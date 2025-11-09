"""
YouTube Analytics API integration for TuneIQ Insight.
Requires channel owner OAuth authentication.
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import pandas as pd
from typing import Dict, Optional
from datetime import datetime, timedelta

# OAuth 2.0 scopes needed for YouTube Analytics
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

def get_youtube_credentials(credentials_json: Dict) -> Optional[Credentials]:
    """
    Get YouTube OAuth credentials.
    Returns None if authentication fails.
    """
    try:
        flow = InstalledAppFlow.from_client_config(
            credentials_json,
            SCOPES
        )
        return flow.run_local_server(port=0)
    except Exception as e:
        print(f"YouTube OAuth Error: {e}")
        return None

def build_youtube_analytics(credentials: Credentials) -> Optional[object]:
    """Build YouTube Analytics API service."""
    try:
        return build('youtubeAnalytics', 'v2', credentials=credentials)
    except Exception as e:
        print(f"YouTube Analytics API Error: {e}")
        return None

def get_geographic_data(youtube: object) -> pd.DataFrame:
    """
    Fetch geographic view data from YouTube Analytics.
    Returns DataFrame with views by country.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    
    try:
        request = youtube.reports().query(
            ids='channel==MINE',
            metrics='estimatedMinutesWatched,views,averageViewDuration',
            dimensions='country',
            startDate=start_date.strftime('%Y-%m-%d'),
            endDate=end_date.strftime('%Y-%m-%d')
        )
        response = request.execute()
        
        # Convert response to DataFrame
        df = pd.DataFrame(response['rows'], 
                         columns=['country', 'watch_minutes', 'views', 'avg_duration'])
        
        # Calculate estimated revenue (very rough approximation)
        # YouTube pays roughly $0.00069 per view on average
        df['reported_revenue_usd'] = df['views'] * 0.00069
        
        # Split into monthly data (approximate)
        months = [
            end_date.strftime('%Y-%m'),
            (end_date - timedelta(days=30)).strftime('%Y-%m')
        ]
        
        # Create final DataFrame
        rows = []
        for month in months:
            for _, row in df.iterrows():
                rows.append({
                    'artist': 'Burna Boy',  # Example artist
                    'track': 'Last Last',    # Example track
                    'platform': 'YouTube',
                    'country': row['country'],
                    'streams': int(row['views'] / 2),  # Split views between months
                    'month': month,
                    'reported_revenue_usd': row['reported_revenue_usd'] / 2  # Split revenue
                })
        
        return pd.DataFrame(rows)
    
    except Exception as e:
        print(f"YouTube Analytics Data Error: {e}")
        return pd.DataFrame()

def get_youtube_analytics(credentials_json: Dict, artist_name: Optional[str] = None) -> pd.DataFrame:
    """
    Main function to fetch YouTube Analytics data.
    Returns DataFrame with geographic view data and estimated revenue.
    """
    credentials = get_youtube_credentials(credentials_json)
    if not credentials:
        return pd.DataFrame()
    
    youtube = build_youtube_analytics(credentials)
    if not youtube:
        return pd.DataFrame()
    
    df = get_geographic_data(youtube)
    # Label artist if provided
    if not df.empty and artist_name:
        df['artist'] = artist_name
    return df