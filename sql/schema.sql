CREATE SCHEMA IF NOT EXISTS analytics;

SET search_path TO analytics;

CREATE TABLE analytics.dim_stock (
    ticker VARCHAR(10) PRIMARY KEY,
    sector VARCHAR(100),
    industry VARCHAR(100)
);

CREATE TABLE analytics.dim_date (
    date DATE PRIMARY KEY,
    month INT,
    quarter INT,
    year INT
);

CREATE TABLE analytics.fact_portfolio_metrics (
    date DATE REFERENCES analytics.dim_date(date),
    ticker VARCHAR(10) REFERENCES analytics.dim_stock(ticker),
    close_price NUMERIC(12,2),
    daily_return NUMERIC(10,6),
    rolling_volatility NUMERIC(10,6),
    sharpe_ratio NUMERIC(10,6),
    var_95 NUMERIC(10,6),
    pnl NUMERIC(12,2),
    PRIMARY KEY (date, ticker)
);

CREATE INDEX idx_fact_ticker ON analytics.fact_portfolio_metrics(ticker);
CREATE INDEX idx_fact_date ON analytics.fact_portfolio_metrics(date);



