"""
Economic Impact & Job Creation Module

Displays AI-powered predictions for GDP contribution and job creation
based on streaming data from APIs or web scraping.
"""

import streamlit as st
import pandas as pd
from typing import Optional, Dict
import importlib

# Import predictor and data pipeline
try:
    # Try package-style imports first
    dp = importlib.import_module("tuneiq_app.data_pipeline")
    get_model_predictions = getattr(dp, "get_model_predictions")
    load_sample_data = getattr(dp, "load_sample_data")
    fetch_live_data = getattr(dp, "fetch_live_data")
    na_mod = importlib.import_module("tuneiq_app.nigerian_artists")
    NIGERIAN_ARTISTS = getattr(na_mod, "NIGERIAN_ARTISTS")
except Exception:
    # Fallback to direct imports
    try:
        dp = importlib.import_module("data_pipeline")
        get_model_predictions = getattr(dp, "get_model_predictions")
        load_sample_data = getattr(dp, "load_sample_data")
        fetch_live_data = getattr(dp, "fetch_live_data")
        na_mod = importlib.import_module("nigerian_artists")
        NIGERIAN_ARTISTS = getattr(na_mod, "NIGERIAN_ARTISTS")
    except Exception as e:
        raise ImportError(
            "Could not import data_pipeline and nigerian_artists functions. "
            "Run from project root or install package."
        ) from e

# Modern dashboard CSS styling
st.markdown("""
<style>
/* Light theme background */
body, [class*="stAppViewContainer"] {
    background-color: #f7f9fc;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* Main card styling */
.main-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    padding: 20px;
    margin-bottom: 25px;
    border: 1px solid rgba(14, 165, 164, 0.1);
}

/* KPI card styling */
.kpi-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(14, 165, 164, 0.1);
    transition: all 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(14, 165, 164, 0.15);
}

/* Metric value styling */
.metric-value {
    font-size: 2.2rem;
    font-weight: 700;
    color: #0EA5A4;
    margin: 10px 0;
}

.metric-label {
    font-size: 0.9rem;
    color: #64748B;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-change {
    font-size: 0.85rem;
    margin-top: 8px;
    font-weight: 600;
}

/* Section styling */
.section-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1F213A;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Expander card styling */
.streamlit-expanderHeader {
    background-color: rgba(14, 165, 164, 0.05) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(14, 165, 164, 0.1) !important;
}

.streamlit-expanderHeader:hover {
    background-color: rgba(14, 165, 164, 0.08) !important;
}
</style>
""", unsafe_allow_html=True)

def format_currency(value: Optional[float]) -> str:
    """Format value as Nigerian Naira currency."""
    if value is None:
        return "N/A"
    return f"₦{value:,.0f}"


def format_number(value: Optional[float]) -> str:
    """Format value as integer with commas."""
    if value is None:
        return "N/A"
    return f"{int(value):,}"


def display_economic_impact_section():
    """
    Render the AI Economic Impact & Job Creation section with modern card styling.
    
    Allows users to:
    1. Select data source (Sample, Spotify, YouTube, Web Scraper)
    2. Select artist from dropdown
    3. Run predictions using the pre-trained model
    4. Display predicted GDP contribution and jobs created in modern KPI cards
    """
    
    # Section header
    st.markdown('<div class="section-header">🎵 Economic Impact & Job Creation</div>', unsafe_allow_html=True)
    st.markdown(
        "Use AI to estimate GDP contribution and job creation from streaming data. "
        "Select a data source and artist below."
    )
    
    # Input section with modern card styling
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Create two columns for input controls
    col1, col2 = st.columns(2)
    
    with col1:
        data_source = st.radio(
            "📊 Select Data Source",
            options=["Sample", "Spotify", "YouTube", "Web Scraper"],
            horizontal=False,
            help="Choose where to fetch data for predictions"
        )
    
    with col2:
        # Get current artist from session state (set in main dashboard)
        # Default to first artist if not set
        default_artist = st.session_state.get('filter_artist', NIGERIAN_ARTISTS[0] if NIGERIAN_ARTISTS else 'Burna Boy')
        default_index = NIGERIAN_ARTISTS.index(default_artist) if default_artist in NIGERIAN_ARTISTS else 0
        
        # Artist dropdown selection
        artist_name = st.selectbox(
            "🎤 Select Artist",
            options=NIGERIAN_ARTISTS,
            index=default_index,
            key="ai_artist_selector",
            help="Choose a Nigerian artist to analyze"
        )
    
    # Run prediction button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    with col_btn1:
        run_prediction = st.button(
            "🚀 Run Prediction",
            use_container_width=True,
            key="run_prediction_btn"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if run_prediction and artist_name:
        with st.spinner(f"🔄 Analyzing {artist_name}..."):
            try:
                # Fetch data based on selected source
                if data_source == "Sample":
                    df = load_sample_data()
                    st.info(f"📊 Using sample data")
                elif data_source == "Web Scraper":
                    df = fetch_live_data(source="web", artist_name=artist_name)
                    if df.empty:
                        st.warning(f"⚠️ No web data found for {artist_name}. Using sample data instead.")
                        df = load_sample_data()
                else:
                    # Spotify or YouTube require API credentials
                    source_lower = data_source.lower()
                    df = fetch_live_data(source=source_lower, artist_name=artist_name)
                    if df.empty:
                        st.warning(
                            f"⚠️ No {data_source} data found. "
                            f"Ensure API credentials are configured. "
                            f"Using sample data instead."
                        )
                        df = load_sample_data()
                
                # Run model prediction
                predictions = get_model_predictions(df)
                
                # Display results
                if predictions.get("error"):
                    error_msg = predictions['error']
                    st.error(f"❌ Prediction Error: {error_msg}")
                    
                    # Show helpful troubleshooting message
                    if "Model could not be loaded" in error_msg:
                        st.warning("""
                        **Model Loading Issue**: The ML model file may not be found or loaded correctly.
                        
                        ℹ️ **Troubleshooting**:
                        1. Ensure `tuneiq_gdp_jobs_model.joblib` exists in the project directory
                        2. Check that the file is not corrupted
                        3. Try running the dashboard from the project root: `cd c:\\tuneiq_app && streamlit run app.py`
                        4. Check the terminal output for detailed error logs
                        """)
                else:
                    st.success(f"✅ Predictions generated for {artist_name}")
                    
                    # Display KPI metrics in modern cards
                    st.markdown('<div class="main-card">', unsafe_allow_html=True)
                    st.markdown("####  AI Predicted Impact Metrics")
                    
                    kpi_cols = st.columns(3)
                    
                    with kpi_cols[0]:
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">💰 GDP Contribution</div>
                            <div class="metric-value">{format_currency(predictions.get('predicted_gdp'))}</div>
                            <div class="metric-change">Nigeria (NGN)</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with kpi_cols[1]:
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">👥 Jobs Created</div>
                            <div class="metric-value">{format_number(predictions.get('predicted_jobs'))}</div>
                            <div class="metric-change">Direct Impact</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with kpi_cols[2]:
                        confidence = predictions.get("confidence", 0)
                        confidence_pct = (confidence * 100) if confidence else 0
                        confidence_color = "#10b981" if confidence_pct >= 80 else "#f59e0b" if confidence_pct >= 60 else "#ef4444"
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">🎯 Confidence</div>
                            <div class="metric-value" style="color: {confidence_color};">{confidence_pct:.0f}%</div>
                            <div class="metric-change">Model Accuracy</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Show data summary
                    st.markdown('<div class="main-card">', unsafe_allow_html=True)
                    st.markdown("#### Input Data Summary")
                    
                    summary_cols = st.columns(3)
                    
                    with summary_cols[0]:
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">Total Records</div>
                            <div class="metric-value">{len(df):,}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with summary_cols[1]:
                        total_streams = df['streams'].sum() if 'streams' in df.columns else 0
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">Total Streams</div>
                            <div class="metric-value">{format_number(total_streams)}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with summary_cols[2]:
                        unique_countries = df['country'].nunique() if 'country' in df.columns else 0
                        st.markdown(f"""
                        <div class="kpi-card">
                            <div class="metric-label">Countries</div>
                            <div class="metric-value">{unique_countries:,}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Show data preview
                    with st.expander("📋 Data Preview", expanded=False):
                        display_cols = ['artist', 'streams', 'country', 'platform', 'month']
                        available_cols = [col for col in display_cols if col in df.columns]
                        st.dataframe(df[available_cols].head(10), use_container_width=True)
            
            except Exception as e:
                st.error(f"❌ Error during prediction: {str(e)}")
    
    elif run_prediction:
        st.warning("⚠️ Please select an artist")
    
    # Add information box
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    with st.expander("ℹ️ About AI Economic Impact Predictions", expanded=False):
        st.markdown("""
        ### How It Works
        TuneIQ uses a pre-trained machine learning model (`tuneiq_gdp_jobs_model.joblib`) 
        to analyze streaming data and estimate:
        
        - **GDP Contribution (₦)**: Estimated direct economic value added to Nigeria's GDP
        - **Jobs Created**: Estimated number of jobs supported by music streaming
        
        ### Data Sources
        - **Sample**: Demonstration data for various artists
        - **Spotify**: Live streaming data from Spotify API
        - **YouTube**: Video view data from YouTube Analytics
        - **Web Scraper**: Real-time trends from web sources
        
        ### Methodology
        The model analyzes:
        1. Total streams and platform diversity
        2. Geographic distribution of streams
        3. Historical streaming patterns
        
        ### Limitations
        - Predictions are estimates based on available data
        - Actual GDP impact depends on many external factors
        - API data may be limited or incomplete for some artists
        
        ### Privacy
        All data is processed locally and anonymized at the country level.
        """)
    st.markdown('</div>', unsafe_allow_html=True)
