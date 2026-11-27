-- Create table unique_id with default id of 1 and UNIQUE constraint if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
