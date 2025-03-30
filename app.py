import pandas as pd
import sqlite3

def setup_database():
    # Connect to the SQLite database (creates trades.db if it doesn't exist)
    conn = sqlite3.connect("trades.db")
    
    # Create a cursor to execute SQL commands
    cursor = conn.cursor()
    
    # Create the trades table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            ticker TEXT,
            date TEXT,
            price REAL,
            quantity INTEGER,
            action TEXT
        )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def log_trade(ticker, date, price, quantity, action):
    # Connect to the database
    conn = sqlite3.connect("trades.db")
    
    # Create a DataFrame with the trade data
    trade = {"ticker": ticker, "date": date, "price": price, "quantity": quantity, "action": action}
    df = pd.DataFrame([trade])
    
    # Insert the trade into the trades table
    df.to_sql("trades", conn, if_exists="append", index=False)
    
    # Close the connection
    conn.close()

def get_trades():
    # Connect to the database
    conn = sqlite3.connect("trades.db")
    
    # Fetch all trades into a DataFrame
    df = pd.read_sql_query("SELECT * FROM trades", conn)
    
    # Close the connection
    conn.close()
    
    # Return the DataFrame
    return df

# Run the setup function to initialize the database
setup_database()

# Test the functions
if __name__ == "__main__":
    # Log a sample trade
    log_trade("AAPL", "2025-03-29", 150.25, 10, "buy")
    
    # Retrieve and display trades
    trades = get_trades()
    print(trades)