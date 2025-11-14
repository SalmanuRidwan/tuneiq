# 🚀 Quick Start - ML Model Integration

## 5-Minute Setup

### Step 1: Install Dependencies
```powershell
cd c:\tuneiq_app
pip install -r requirements.txt
```

### Step 2: Run Dashboard
```powershell
streamlit run app.py
```

### Step 3: Find AI Predictions
Scroll to the **bottom** of the dashboard for:
```
🤖 AI-Powered Economic Impact Predictions
```

### Step 4: Run a Prediction
1. Select "Sample" as data source
2. Enter "Burna Boy" as artist
3. Click "🚀 Run AI Prediction"
4. View results!

## Expected Output

```
✅ Predictions generated for Burna Boy

💰 Predicted GDP Contribution (₦): ₦[amount]
👥 Predicted Jobs Created: [number]
```

## Files You Need to Know

| File | Purpose |
|------|---------|
| `predictor.py` | Loads & runs ML model |
| `economic_impact.py` | Dashboard UI for predictions |
| `data_pipeline.py` | Connects data to model |
| `app.py` | Main dashboard (displays predictions) |
| `tuneiq_gdp_jobs_model.joblib` | Pre-trained model (use as-is) |

## Python Usage

```python
# Quick prediction
from data_pipeline import load_sample_data, get_model_predictions

df = load_sample_data()
predictions = get_model_predictions(df)

print(f"GDP: ₦{predictions['predicted_gdp']:,.0f}")
print(f"Jobs: {int(predictions['predicted_jobs']):,}")
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| ModuleNotFoundError: joblib | `pip install joblib>=1.2.0` |
| Model not found | `cd c:\tuneiq_app` (run from project root) |
| Import errors | `pip install -e .` (install as package) |
| Nothing appears on dashboard | Scroll to bottom of page |

## Data Sources for Predictions

- **Sample**: Demo data (always works)
- **Spotify**: Requires Spotify API credentials
- **YouTube**: Requires YouTube API credentials  
- **Web Scraper**: Works without credentials

## Integration Verification

Run this Python code to verify everything is set up:

```python
# Test 1: Load model
from predictor import load_tuneiq_model
model = load_tuneiq_model()
print(f"✓ Model loaded: {model is not None}")

# Test 2: Get predictions
from data_pipeline import load_sample_data, get_model_predictions
df = load_sample_data()
pred = get_model_predictions(df)
print(f"✓ Predictions: GDP={pred['predicted_gdp']}, Jobs={pred['predicted_jobs']}")

# Test 3: Display function
from economic_impact import display_economic_impact_section
print(f"✓ UI module loaded: {display_economic_impact_section is not None}")
```

## What the Model Does

### Inputs:
- Streaming data (views/streams count)
- Country distribution
- Platform diversity

### Outputs:
- **GDP Contribution**: ₦[estimated value]
- **Jobs Created**: [estimated count]
- **Confidence**: [0-1 score if available]

## Key Features

✅ Works with sample data (no API needed)
✅ Supports live data from multiple platforms
✅ Web scraping fallback
✅ Error handling & logging
✅ Formatted currency display
✅ Data preview & summary

## Next Steps

1. **Test with sample data** (5 minutes)
2. **Try with live data** (configure API credentials)
3. **Review predictions** against your expectations
4. **Explore different artists** via web scraper

## Documentation

- **Quick Start**: This file
- **Full Setup**: README.md
- **Testing**: INTEGRATION_TEST.md
- **Summary**: ML_INTEGRATION_SUMMARY.md
- **Code Docs**: See docstrings in predictor.py, economic_impact.py

## Support

If something doesn't work:

1. Check `INTEGRATION_TEST.md` for troubleshooting
2. Review `predictor.py` docstrings
3. Check Streamlit console for error messages
4. Ensure you're in the `c:\tuneiq_app` directory

## Done! 🎉

The ML model is fully integrated and ready to use.

Just run:
```bash
cd c:\tuneiq_app
streamlit run app.py
```

Then scroll to the bottom and start making predictions!

