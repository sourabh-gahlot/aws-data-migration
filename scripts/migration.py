import boto3
import os

bucket = "retail-migration-lab-2026-12345"
folder = "data"

s3 = boto3.client("s3")

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if os.path.isfile(filepath):
        s3.upload_file(
            filepath,
            bucket,
            "data/" + filename
        )

        print("Uploaded:", filename)

print("Migration completed!")