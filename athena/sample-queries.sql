-- Preview data
SELECT *
FROM processed_processed_store_events_cloudliz
LIMIT 10;

-- Total amount spent per user
SELECT
  user_id,
  SUM(amount) AS total_spent
FROM processed_processed_store_events_cloudliz
GROUP BY user_id;

-- Event counts
SELECT
  event_type,
  COUNT(*) AS event_count
FROM processed_processed_store_events_cloudliz
GROUP BY event_type;

-- Partition-filtered query
SELECT *
FROM processed_processed_store_events_cloudliz
WHERE year = '2025'
  AND month = '12'
  AND day = '17';

