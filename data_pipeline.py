"""
Data pipeline for TuneIQ Insight - handles both sample and live data sources.
Supports fallback to sample data when API keys aren't configured.
"""

import os
import pandas as pd
from typing import Optional, Dict
from tuneiq_app.spotify_fetch import get_spotify_data
from tuneiq_app.youtube_fetch_oauth import get_youtube_analytics
from tuneiq_app.apple_music_fetch import get_apple_music_data

def load_sample_data() -> pd.DataFrame:
    """Load Burna Boy sample streaming data."""
    sample_path = os.path.join(os.path.dirname(__file__), 'sample_data/streaming_sample.csv')
    return pd.read_csv(sample_path)

def fetch_spotify_data(client_id: Optional[str] = None, 
                      client_secret: Optional[str] = None,
                      artist_name: Optional[str] = None) -> Optional[pd.DataFrame]:
    """
    Fetch Spotify streaming data if credentials provided, else return None.
    Uses client credentials flow (no user auth required).
    """
    if not (client_id and client_secret):
        return None
    
    try:
        return get_spotify_data(client_id, client_secret, artist_name=artist_name)
    except Exception as e:
        print(f"Spotify API Error: {e}")
        return None

def fetch_youtube_geo_data(credentials_json: Optional[Dict] = None,
                          artist_name: Optional[str] = None) -> Optional[pd.DataFrame]:
    """
    Fetch YouTube Analytics geographic data if OAuth credentials provided.
    Requires channel owner authentication.
    """
    if not credentials_json:
        return None
    
    try:
        # Pass artist_name for labeling if supported by the YouTube helper
        return get_youtube_analytics(credentials_json, artist_name=artist_name)
    except Exception as e:
        print(f"YouTube API Error: {e}")
        return None

def fetch_all(spotify_creds: Optional[Dict] = None,
              youtube_creds: Optional[Dict] = None,
              apple_music_creds: Optional[Dict] = None,
              artist_name: Optional[str] = None) -> pd.DataFrame:
    """
    Orchestration function to merge sample and live data when available.
    Falls back to sample data if no API credentials provided.
    """
    # Always load sample data as fallback
    df = load_sample_data()
    
    # Attempt to fetch live data if credentials provided
    if spotify_creds:
        spotify_df = fetch_spotify_data(
            spotify_creds.get('client_id'),
            spotify_creds.get('client_secret'),
            artist_name=artist_name
        )
        if spotify_df is not None:
            # Replace sample Spotify data with live data
            df = df[df['platform'] != 'Spotify'].copy()
            df = pd.concat([df, spotify_df])
    
    if youtube_creds:
        youtube_df = fetch_youtube_geo_data(youtube_creds, artist_name=artist_name)
        if youtube_df is not None:
            # Replace sample YouTube data with live data
            df = df[df['platform'] != 'YouTube'].copy()
            df = pd.concat([df, youtube_df])

    # Apple Music (optional/stub)
    if apple_music_creds:
        try:
            apple_df = get_apple_music_data(apple_music_creds, artist_name=artist_name)
            if apple_df is not None:
                df = df[df['platform'] != 'Apple Music'].copy()
                df = pd.concat([df, apple_df])
        except Exception as e:
            print(f"Apple Music API Error: {e}")
    
    return df.reset_index(drop=True)