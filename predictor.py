import joblib
import pandas as pd
import numpy as np
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "tuneiq_gdp_jobs_model.joblib")

# Define the expected features from your training data
EXPECTED_FEATURES = [
    "Streams Last 30 Days (Millions)",
    "Monthly Listeners (Millions)",
    "Avg Stream Duration (Min)",
    "Skip Rate (%)",
    "Release Year",
    "Playlist Adds",
    "Followers (Millions)",
    "Engagement Rate (%)"
]

def load_tuneiq_model():
    """Load the trained TuneIQ GDP/Jobs model."""
    try:
        model = joblib.load(MODEL_PATH)
        logger.info(f"✅ Model loaded successfully from {MODEL_PATH}")
        return model
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")
        return None


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform scraped or API data to match the model's expected input schema.
    Missing features are filled with mean-like or neutral defaults.
    """
    # Create a new DataFrame with the expected columns
    data = {}

    # Map what you have to what the model expects (adjust as needed)
    # Example mappings based on typical streaming data fields
    data["Streams Last 30 Days (Millions)"] = (
        df["streams"].sum() / 1_000_000 if "streams" in df.columns else 0.5
    )
    data["Monthly Listeners (Millions)"] = (
        df["listeners"].mean() / 1_000_000 if "listeners" in df.columns else 2.0
    )
    data["Avg Stream Duration (Min)"] = (
        df["duration"].mean() / 60 if "duration" in df.columns else 3.5
    )
    data["Skip Rate (%)"] = df.get("skip_rate", pd.Series([5])).mean()
    data["Release Year"] = int(df.get("release_year", pd.Series([2023])).mean())
    data["Playlist Adds"] = df.get("playlist_adds", pd.Series([10])).mean()
    data["Followers (Millions)"] = df.get("followers", pd.Series([1.0])).mean()
    data["Engagement Rate (%)"] = df.get("engagement_rate", pd.Series([20])).mean()

    # Return as a single-row DataFrame with the correct feature order
    feature_df = pd.DataFrame([data])[EXPECTED_FEATURES]
    logger.info(f"Prepared features for prediction: {feature_df.columns.tolist()}")
    return feature_df


def predict_impact(df: pd.DataFrame):
    """
    Use the trained model to predict GDP and job creation.
    """
    model = load_tuneiq_model()
    if model is None:
        return {"predicted_gdp": None, "predicted_jobs": None}

    try:
        X = prepare_features(df)
        y_pred = model.predict(X)

        # Handle single-output or multi-output models
        if isinstance(y_pred[0], (list, np.ndarray)) and len(y_pred[0]) >= 2:
            return {
                "predicted_gdp": float(y_pred[0][0]),
                "predicted_jobs": float(y_pred[0][1]),
            }
        else:
            return {
                "predicted_gdp": float(y_pred[0]),
                "predicted_jobs": None,
            }
    except Exception as e:
        logger.error(f"❌ Prediction Error: {e}")
        return {"predicted_gdp": None, "predicted_jobs": None}
