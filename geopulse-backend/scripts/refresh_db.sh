#!/bin/bash

# Create a directory for temp zip files
TEMP_DIR="/tmp/geopulse"
HISTORY="history.txt"
mkdir -p $TEMP_DIR

# URL of the lastupdate.txt file
LASTUPDATE_URL="http://data.gdeltproject.org/gdeltv2/lastupdate.txt"

# Download the lastupdate.txt file
curl -s -o lastupdate.txt $LASTUPDATE_URL

# Extract the .export.CSV.zip URLs from the lastupdate.txt file
EXPORT_URLS=$(grep '.export.CSV.zip' lastupdate.txt | awk '{print $3}')
cat lastupdate.txt >> "$TEMP_DIR/$HISTORY"
# Download each .export.CSV.zip file and unzip it into the temp directory
for URL in $EXPORT_URLS; do
    # Get the file name from the URL
    FILE_NAME=$(basename $URL)

    # Download the zip file
    curl -s -o $TEMP_DIR/$FILE_NAME $URL

    # Unzip the file into the temp directory
    unzip -o $TEMP_DIR/$FILE_NAME -d $TEMP_DIR
done

# Clean up the lastupdate.txt file
rm lastupdate.txt

echo "Download and extraction complete. Files are located in the $TEMP_DIR directory."

# Add the script to the crontab if it doesn't already exist
SCRIPT_PATH="$(pwd)/$(basename "$0")"
CRON_JOB="*/15 * * * * $SCRIPT_PATH"
(crontab -l | grep -F "$CRON_JOB") || (crontab -l; echo "$CRON_JOB") | crontab -
