#!/bin/bash

# Configuration variables
PYTHON_SCRIPT_PATH="./web_scraper.py"  # Update this path
INTERVAL_HOURS=23  # Time interval in hours (must be 1-23) Recommonded: 23 so that not to get banned
LOG_FILE="/var/log/tuneiq_cron.log"  # Optional: log file path

# Validate inputs
if [[ ! -f "$PYTHON_SCRIPT_PATH" ]]; then
    echo "Error: Python script not found at $PYTHON_SCRIPT_PATH"
    exit 1
fi

if ! [[ "$INTERVAL_HOURS" =~ ^[0-9]+$ ]] || [ "$INTERVAL_HOURS" -lt 1 ] || [ "$INTERVAL_HOURS" -gt 23 ]; then
    echo "Error: INTERVAL_HOURS must be an integer between 1 and 23"
    exit 1
fi

# Get absolute path to python3 (recommended)
PYTHON_PATH=$(which python3)
if [[ -z "$PYTHON_PATH" ]]; then
    echo "Error: python3 not found in PATH"
    exit 1
fi

# Create cron job entry
CRON_JOB="0 */$INTERVAL_HOURS * * * $PYTHON_PATH $PYTHON_SCRIPT_PATH >> $LOG_FILE 2>&1"

# Add job to crontab (with safety check)
(
    crontab -l 2>/dev/null
    echo "$CRON_JOB"
) | crontab -

echo "Cron job added successfully!"
echo "Will run every $INTERVAL_HOURS hours at minute 0"
echo "Command: $CRON_JOB"
