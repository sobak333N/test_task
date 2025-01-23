CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    articule BIGINT UNIQUE NOT NULL,
    cost BIGINT NOT NULL,
    rating FLOAT NOT NULL,
    total_quantity INTEGER NOT NULL
);

CREATE INDEX idx_products_articule ON products (articule);
