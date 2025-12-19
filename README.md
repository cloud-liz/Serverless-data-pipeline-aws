# Serverless Data Pipeline on AWS

This project demonstrates a serverless, event-driven data pipeline using AWS services.

## Architecture
- S3 for raw and processed data storage
- Lambda for data transformation
- Glue Crawler for schema discovery
- Athena for SQL analytics

## Data Flow
1. CSV file uploaded to raw S3 bucket
2. Lambda triggered by S3 PUT event
3. Lambda cleans and structures data
4. Processed data written to partitioned S3 paths
5. Glue crawler discovers schema
6. Athena queries data directly from S3

## Technologies Used
- AWS S3
- AWS Lambda (Python)
- AWS Glue
- AWS Athena
- IAM

## Example Queries
See `athena/sample-queries.sql`

## Why This Architecture
- No servers to manage
- Pay-per-query analytics
- Scales automatically
- Ideal for append-only analytical workloads
