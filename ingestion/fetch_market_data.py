import psycopg2
from datetime import datetime

def insert_data():
    # Connect to the PostgreSQL database
   conn = psycopg2.connect(
      host="postgres",
      database="riskdb",
      user="admin",
      password="admin123"
   )

   cursor = conn.cursor()

   # Insert stock
   cursor.execute("""
                  INSERT INTO analytics.dim_stock (ticker, sector, industry)
                  VALUES (%s, %s, %s)
                  ON CONFLICT (ticker) DO NOTHING;
                  """, ("AAPL", "Technology", "Consumer Electronics"))
   
   # Insert date
   today = datetime.today().date()

   cursor.execute("""
                   INSERT INTO analytics.dim_date (date, month, quarter, year)
                   VALUES (%s, %s, %s, %s)
                  ON CONFLICT (date) DO NOTHING;
                  """, (today, today.month, (today.month-1)//3 + 1, today.year))
   
   # Insert fact
   cursor.execute("""
                  INSERT INTO analytics.fact_portfolio_metrics
                  (date, ticker, close_price, daily_return,
                  rolling_volatility, sharpe_ratio, var_95, pnl)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                  ON CONFLICT (date, ticker) DO NOTHING;
                  """, (today, "AAPL", 180.00, 0.012, 0.25, 1.5, -0.03, 1200.00))
   
   conn.commit()
   cursor.close()
   conn.close()


if __name__ == "__main__":
   insert_data()
