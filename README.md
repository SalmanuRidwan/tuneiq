# TuneIQ Insight

Making Nigeria's music economy visible through data-driven analytics.

## Hackathon Project Overview

TuneIQ Insight addresses a critical gap in Nigeria's music industry: the lack of transparent, accessible data about our music's global reach and economic impact. By aggregating and analyzing streaming data across platforms, we make visible the true scale of Nigeria's cultural exports and highlight areas where value capture can be improved.

### Key Features

- **Multi-Platform Analytics**: Aggregates data from Spotify, YouTube, and Apple Music
- **Interactive Dashboard**: Intuitive UI with toggleable sections for focused analysis
- **Economic Impact Tracking**: Estimates direct revenue, indirect benefits, and cultural export value
- **Revenue Gap Analysis**: Identifies potential underpayment regions for investigation
- **Privacy-First Design**: Uses only country-level aggregated data, no personal information
- **Flexible Data Sources**: 
  - Sample Mode: Uses example data for demos and testing
  - Live Mode: Connects to real platform APIs when credentials are provided
- **Platform Performance Comparison**: Compare streaming metrics across different platforms
- **Dynamic Data Pipeline**: Robust data processing with automated tests

## Privacy & Data Handling

TuneIQ Insight is designed with privacy in mind:
- Only processes country-level aggregated data
- No individual user data or PII is collected
- All analysis happens locally in your environment
- API credentials are never stored, only used in memory during live sessions

## Setup Instructions

1. Create a Python virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/MacOS
```

2. Install dependencies:
```powershell
pip install -e .  # Install in development mode
pip install -r requirements.txt
```

3. Run tests (optional but recommended):
```powershell
pytest tests/
```

4. Run the dashboard:
```powershell
streamlit run app.py
```

The app will start in Sample Mode by default, using example streaming history data.

## Using Live Data Mode

To enable live data fetching:

1. **Spotify API Setup**:
   - Create a Spotify Developer account
   - Create an application to get Client ID and Secret
   - Enter credentials in the dashboard's Live Mode section

2. **YouTube Analytics API Setup**:
   - Set up a Google Cloud Project
   - Enable YouTube Analytics API
   - Create OAuth 2.0 credentials
   - Download and paste the credentials JSON in the dashboard

3. **Apple Music API Setup**:
   - Get an Apple Music Developer Token
   - Configure the token in the dashboard's Live Mode section

## Contributing

This project is part of our effort to bring transparency to Nigeria's music economy. We welcome contributions that help:
- Improve data accuracy
- Add new platforms
- Enhance visualizations
- Expand economic impact analysis

## License

MIT License - See LICENSE file for details