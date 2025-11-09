from setuptools import setup, find_packages

setup(
    name="tuneiq_app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "plotly",
        "spotipy",
        "google-api-python-client",
        "google-auth-oauthlib",
        "python-dotenv",
    ],
)