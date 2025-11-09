"""
Apple Music helper (minimal stub).

This module provides a placeholder `get_apple_music_data` function that can be
extended to call the Apple Music API (MusicKit) using a developer token (JWT).

Implementing a full Apple Music integration requires generating a signed JWT
from your private key and using the Music API endpoints. For now the function
returns None when no implementation is present to preserve current behavior.
"""
from typing import Optional, Dict
import pandas as pd
import time
import logging

try:
    import jwt  # PyJWT
except Exception:
    jwt = None
 
try:
    import requests
except Exception:
    requests = None

logger = logging.getLogger(__name__)


def _build_developer_token_from_key(key_id: str, team_id: str, private_key: str, expire_seconds: int = 3600) -> Optional[str]:
    """Create an Apple Music developer token (JWT) from key material.

    This requires PyJWT to be installed. If PyJWT is not available, returns None.
    """
    if jwt is None:
        logger.debug("PyJWT not available; cannot build developer token from private key.")
        return None

    headers = {
        'alg': 'ES256',
        'kid': key_id
    }
    now = int(time.time())
    payload = {
        'iss': team_id,
        'iat': now,
        'exp': now + expire_seconds
    }

    try:
        token = jwt.encode(payload, private_key, algorithm='ES256', headers=headers)
        # PyJWT returns bytes in some versions; ensure str
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        return token
    except Exception as e:
        logger.exception("Failed to create Apple Music developer token: %s", e)
        return None


def get_apple_music_data(creds: Dict, artist_name: Optional[str] = None) -> Optional[pd.DataFrame]:
    """Fetch Apple Music streaming/artist data.

    Accepts two credential patterns in `creds`:
    - {'developer_token': '<token>'}
    - {'key_id': ..., 'team_id': ..., 'private_key': '-----BEGIN PRIVATE KEY-----...'}

    The function will attempt to build a developer token if needed. For safety
    this implementation does not make network requests; it returns None so the
    caller falls back to sample data. The token-building helper is provided so
    you can extend the function to call the Music API later.
    """
    if not creds:
        return None

    developer_token = creds.get('developer_token')
    if not developer_token:
        # Try to generate from private key material
        key_id = creds.get('key_id')
        team_id = creds.get('team_id')
        private_key = creds.get('private_key')
        if key_id and team_id and private_key:
            developer_token = _build_developer_token_from_key(key_id, team_id, private_key)

    if not developer_token:
        logger.info("No Apple Music developer token available; skipping Apple Music fetch.")
        return None
    # At this point we have a developer token. Attempt a light-weight catalog
    # search for the artist and their top songs (storefront default: 'us').
    if requests is None:
        logger.warning("requests package not available; cannot call Apple Music API.")
        return None

    storefront = creds.get('storefront', 'us')
    if not artist_name:
        logger.info("No artist_name provided for Apple Music search; skipping.")
        return None

    search_url = f"https://api.music.apple.com/v1/catalog/{storefront}/search"
    headers = {"Authorization": f"Bearer {developer_token}"}
    params = {
        'term': artist_name,
        'types': 'artists,songs',
        'limit': 5
    }

    try:
        resp = requests.get(search_url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        rows = []
        # If artist present, extract artist attributes
        artists = data.get('results', {}).get('artists', {}).get('data', [])
        songs = data.get('results', {}).get('songs', {}).get('data', [])

        artist_attr = None
        if len(artists) > 0:
            artist_attr = artists[0].get('attributes', {})

        # Build rows for each song found (best-effort mapping)
        for s in songs:
            attrs = s.get('attributes', {})
            title = attrs.get('name')
            artist = attrs.get('artistName') or (artist_attr.get('name') if artist_attr else artist_name)
            artwork = None
            art = attrs.get('artwork') or (artist_attr.get('artwork') if artist_attr else None)
            if art:
                # artwork has url with placeholders {w}x{h}
                artwork_url = art.get('url')
                if artwork_url:
                    artwork = artwork_url.replace('{w}', '500').replace('{h}', '500')

            # We don't get streams from the Catalog API; set streams to 0 so the
            # rest of the pipeline can still operate and fall back to sample data as needed.
            rows.append({
                'platform': 'Apple Music',
                'artist': artist,
                'country': storefront.upper(),
                'month': time.strftime('%Y-%m'),
                'streams': 0,
                'track': title,
                'artist_image': artwork,
                'expected_revenue_ngn': 0.0,
                'actual_revenue_ngn': 0.0
            })

        if len(rows) == 0:
            logger.info("Apple Music search returned no songs for '%s'", artist_name)
            return None

        df = pd.DataFrame(rows)
        return df

    except Exception as e:
        logger.exception("Apple Music API call failed: %s", e)
        return None
