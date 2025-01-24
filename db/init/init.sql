CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    artikul BIGINT UNIQUE NOT NULL,
    cost BIGINT NOT NULL,
    rating FLOAT NOT NULL,
    total_quantity INTEGER NOT NULL
);

CREATE INDEX idx_products_artikul ON products (artikul);

CREATE TABLE apscheduler_jobs (
    id VARCHAR(191) NOT NULL PRIMARY KEY,
    next_run_time TIMESTAMP WITH TIME ZONE NULL,
    job_state BYTEA NOT NULL
);

CREATE INDEX idx_apscheduler_jobs_next_run_time ON apscheduler_jobs (next_run_time);
