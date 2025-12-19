import boto3
import csv
import io
from datetime import datetime

s3 = boto3.client("s3")

PROCESSED_BUCKET = "processed-store-events-cloudliz"

def lambda_handler(event, context):
    print("Lambda triggered")

    # 1. Extract bucket and key
    record = event["Records"][0]["s3"]
    raw_bucket = record["bucket"]["name"]
    raw_key = record["object"]["key"]

    print(f"Reading from s3://{raw_bucket}/{raw_key}")

    # 2. Read raw file
    response = s3.get_object(Bucket=raw_bucket, Key=raw_key)
    file_content = response["Body"].read().decode("utf-8")

    # 3. Parse CSV
    csv_input = io.StringIO(file_content)
    reader = csv.reader(csv_input)

    rows = list(reader)

    # 4. Add header
    header = ["date", "user_id", "event_type", "amount"]
    output_rows = [header] + rows

    # 5. Build processed S3 path
    now = datetime.utcnow()
    filename = raw_key.split("/")[-1]

    processed_key = (
        f"year={now.year}/"
        f"month={now.month:02d}/"
        f"day={now.day:02d}/"
        f"{filename}"
    )

    print(f"Writing to s3://{PROCESSED_BUCKET}/{processed_key}")

    # 6. Write processed CSV
    csv_output = io.StringIO()
    writer = csv.writer(csv_output)
    writer.writerows(output_rows)

    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        Key=processed_key,
        Body=csv_output.getvalue()
    )

    print("Write complete")
