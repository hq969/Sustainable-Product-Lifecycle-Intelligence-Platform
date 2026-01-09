CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(100),
    revision VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE suppliers (
    supplier_name VARCHAR(100) PRIMARY KEY,
    esg_score DECIMAL(5,2),
    certified BOOLEAN
);

CREATE TABLE carbon_ledger (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(50),
    lifecycle_stage VARCHAR(50),
    emissions_kgco2e DECIMAL(10,2),
    cost_usd DECIMAL(10,2),
    verified BOOLEAN DEFAULT FALSE
);

CREATE TABLE scope3_emissions (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(50),
    supplier_name VARCHAR(100),
    emissions_kgco2e DECIMAL(10,2),
    category VARCHAR(50)
);
