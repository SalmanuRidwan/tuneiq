import sys
import os
import unittest
import pandas as pd

# Ensure the parent of the package is on sys.path so 'import tuneiq_app' works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from tuneiq_app.data_pipeline import fetch_all


class TestDataPipeline(unittest.TestCase):
    def test_fetch_all_returns_dataframe(self):
        df = fetch_all()
        self.assertIsInstance(df, pd.DataFrame)
        # Basic expected columns from sample pipeline
        self.assertIn('platform', df.columns)
        self.assertIn('streams', df.columns)
        # Should have at least one row in sample data
        self.assertGreaterEqual(len(df), 1)


if __name__ == '__main__':
    unittest.main()
