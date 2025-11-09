"""
Models for TuneIQ Insight - handles revenue estimation, underpayment detection,
and economic impact analysis.
"""

import pandas as pd
import numpy as np
from typing import Dict

# Platform-specific streaming rates (USD)
STREAM_RATES = {
    'Spotify': 0.004,
    'YouTube': 0.00069,
    'Apple Music': 0.01
}

# USD to NGN conversion rate
NGN_RATE = 850  # Example rate, should be updated regularly

def estimate_royalties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate expected revenue based on per-platform streaming rates.
    Returns DataFrame with new columns:
    - expected_revenue_usd: Calculated from streams * platform rate
    - expected_revenue_ngn: USD converted to NGN
    - actual_revenue_ngn: Reported revenue converted to NGN
    """
    df = df.copy()
    
    # Calculate expected revenue
    df['expected_revenue_usd'] = df.apply(
        lambda row: row['streams'] * STREAM_RATES.get(row['platform'], 0.003),
        axis=1
    )
    
    # Convert to NGN
    df['expected_revenue_ngn'] = df['expected_revenue_usd'] * NGN_RATE
    df['actual_revenue_ngn'] = df['reported_revenue_usd'] * NGN_RATE
    
    return df

def detect_underpayment(df: pd.DataFrame, threshold: float = 0.15) -> pd.DataFrame:
    """
    Compare actual vs expected revenue to identify potential underpayment.
    threshold: Maximum acceptable deviation (e.g., 0.15 = 15% below expected)
    
    Returns DataFrame with underpaid regions, sorted by severity.
    """
    df = estimate_royalties(df)
    
    # Calculate underpayment percentage
    df['underpayment_pct'] = (
        (df['expected_revenue_ngn'] - df['actual_revenue_ngn']) 
        / df['expected_revenue_ngn']
    )
    
    # Filter for significant underpayments
    underpaid = df[df['underpayment_pct'] > threshold].copy()
    
    # Group by country and calculate severity metrics
    severity = underpaid.groupby('country').agg({
        'underpayment_pct': 'mean',
        'expected_revenue_ngn': 'sum',
        'actual_revenue_ngn': 'sum',
        'streams': 'sum'
    }).reset_index()
    
    severity['lost_revenue_ngn'] = (
        severity['expected_revenue_ngn'] - severity['actual_revenue_ngn']
    )
    
    return severity.sort_values('lost_revenue_ngn', ascending=False)

def economic_impact_proxy(df: pd.DataFrame) -> Dict:
    """
    Approximate contribution to national creative economy.
    Uses streaming data to estimate:
    - Direct revenue (from streams)
    - Indirect impact (merchandise, shows)
    - Cultural export value
    
    Returns dict with impact metrics in NGN.
    """
    df = estimate_royalties(df)
    
    # Direct streaming revenue
    direct_revenue = df['actual_revenue_ngn'].sum()
    
    # Estimate indirect revenue (typically 2-3x streaming revenue)
    indirect_multiplier = 2.5
    indirect_revenue = direct_revenue * indirect_multiplier
    
    # Cultural export value (non-Nigerian streams have additional impact)
    foreign_streams = df[df['country'] != 'Nigeria']['streams'].sum()
    cultural_export_value = foreign_streams * 0.01 * NGN_RATE  # Rough proxy
    
    return {
        'direct_revenue_ngn': direct_revenue,
        'indirect_revenue_ngn': indirect_revenue,
        'cultural_export_value_ngn': cultural_export_value,
        'total_economic_impact_ngn': direct_revenue + indirect_revenue + cultural_export_value
    }