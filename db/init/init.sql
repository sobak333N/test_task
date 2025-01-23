CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    artikul BIGINT UNIQUE NOT NULL,
    cost BIGINT NOT NULL,
    rating FLOAT NOT NULL,
    total_quantity INTEGER NOT NULL
);

CREATE INDEX idx_products_artikul ON products (artikul);
