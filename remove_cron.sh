#!/bin/bash


PYTHON_SCRIPT_PATH="./web_scraper.py"  # Must match exactly with the one from setup!
LOG_FILE="/var/log/myscript.log"                   # Optional, but helps ensure exact match

# === Safety check ===
if [[ ! -f "$PYTHON_SCRIPT_PATH" ]]; then
    echo "Warning: Python script not found at $PYTHON_SCRIPT_PATH"
    echo "Proceeding anyway to clean up cron job..."
fi

crontab -l 2>/dev/null | grep -vF "$PYTHON_SCRIPT_PATH" | crontab -

echo "Cron job for $PYTHON_SCRIPT_PATH has been removed."
echo "Current cron jobs:"
crontab -l 2>/dev/null || echo "(no cron jobs remaining)"
