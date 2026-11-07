#!/bin/bash

BUCKET="retail-migration-lab-2026-12345"
SOURCE="./data"

echo "Starting AWS Backup..."

aws s3 sync "$SOURCE" "s3://$BUCKET/data/"

if [ $? -ne 0 ]; then
    echo "Backup failed"
    exit 1
fi

echo "Backup completed successfully"
