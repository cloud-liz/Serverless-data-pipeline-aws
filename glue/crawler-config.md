# Glue Crawler Configuration

- Crawler name: processed-store-events-crawler
- Data source: S3
- Path: s3://processed-store-events-cloudliz/
- Database: store_events_db
- Table prefix: processed_
- Partitions detected:
  - year
  - month
  - day
