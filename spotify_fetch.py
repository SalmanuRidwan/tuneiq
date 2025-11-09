"""
Spotify API integration for TuneIQ Insight.
Uses Spotipy with client credentials flow (no user auth required).
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from typing import Optional, Dict
import time
from datetime import datetime, timedelta

def get_spotify_client(client_id: str, client_secret: str) -> spotipy.Spotify:
    """Initialize Spotify client with credentials."""
    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def get_artist_popularity_proxy(sp: spotipy.Spotify, 
                             artist_id: str,
                             scale_factor: float = 1000) -> Dict:
    """
    Get artist popularity and convert to estimated streams.
    Uses popularity * scale_factor as proxy when actual stream count unavailable.
    """
    artist = sp.artist(artist_id)
    popularity = artist['popularity']  # 0-100 scale
    
    # Convert popularity to estimated daily streams per country
    estimated_streams = {
        'Nigeria': int(popularity * scale_factor * 1.5),  # Higher weight for home market
        'United States': int(popularity * scale_factor * 1.2),
        'United Kingdom': int(popularity * scale_factor * 0.8),
        'Ghana': int(popularity * scale_factor * 0.4),
        'South Africa': int(popularity * scale_factor * 0.3)
    }
    
    return estimated_streams

def get_spotify_data(client_id: str, client_secret: str, artist_name: Optional[str] = None) -> pd.DataFrame:
    """
    Fetch Spotify data for a given artist name using client credentials.
    If `artist_name` is provided, attempt to search Spotify for the artist and use their popularity
    as a streams proxy. If search fails, fall back to a default Burna Boy example.
    Returns a DataFrame similar to the sample CSV shape.
    """
    sp = get_spotify_client(client_id, client_secret)

    # Try to resolve artist by name; fall back to Burna Boy if not provided or not found
    default_artist_id = '3wcj11K77LjEY1PkEazffa'  # Burna Boy
    resolved_artist_id = default_artist_id
    resolved_artist_name = 'Burna Boy'

    try:
        if artist_name:
            results = sp.search(q=f'artist:{artist_name}', type='artist', limit=1)
            items = results.get('artists', {}).get('items', [])
            if items:
                resolved_artist_id = items[0]['id']
                resolved_artist_name = items[0]['name']
            else:
                # try a generic search
                results = sp.search(q=artist_name, type='artist', limit=1)
                items = results.get('artists', {}).get('items', [])
                if items:
                    resolved_artist_id = items[0]['id']
                    resolved_artist_name = items[0]['name']

        # Get popularity-based stream estimates
        streams = get_artist_popularity_proxy(sp, resolved_artist_id)

        # Try to obtain artist image if available
        artist_image_url = None
        try:
            artist_obj = sp.artist(resolved_artist_id)
            images = artist_obj.get('images', [])
            if images:
                artist_image_url = images[0].get('url')
        except Exception:
            artist_image_url = None

        # Build DataFrame rows with two months of estimates
        rows = []
        today = datetime.now()
        for month_offset in [0, -1]:
            month = (today + timedelta(days=30*month_offset)).strftime('%Y-%m')
            for country, stream_count in streams.items():
                adjusted_streams = int(stream_count * (0.9 + 0.2 * (time.time() % 1)))
                rows.append({
                    'artist': resolved_artist_name,
                    'track': 'Unknown',
                    'platform': 'Spotify',
                    'country': country,
                    'streams': adjusted_streams,
                    'month': month,
                    'reported_revenue_usd': adjusted_streams * 0.004,
                    'artist_image': artist_image_url
                })
        return pd.DataFrame(rows)

    except Exception as e:
        print(f"Error fetching Spotify data: {e}")
        return pd.DataFrame()