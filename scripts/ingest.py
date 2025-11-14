import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('ecommerce.db')
conn.execute('PRAGMA foreign_keys = ON;')

# Create tables
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    signup_date TEXT,
    city TEXT
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    order_date TEXT,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method TEXT,
    payment_status TEXT,
    amount REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
''')

# Load CSV files
users_df = pd.read_csv('users.csv')
products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')
order_items_df = pd.read_csv('order_items.csv')
payments_df = pd.read_csv('payments.csv')

# Insert data
users_df.to_sql('users', conn, if_exists='replace', index=False)
products_df.to_sql('products', conn, if_exists='replace', index=False)
orders_df.to_sql('orders', conn, if_exists='replace', index=False)
order_items_df.to_sql('order_items', conn, if_exists='replace', index=False)
payments_df.to_sql('payments', conn, if_exists='replace', index=False)

# Commit changes
conn.commit()

# Print row counts
print("users:", conn.execute('SELECT COUNT(*) FROM users;').fetchone()[0])
print("products:", conn.execute('SELECT COUNT(*) FROM products;').fetchone()[0])
print("orders:", conn.execute('SELECT COUNT(*) FROM orders;').fetchone()[0])
print("order_items:", conn.execute('SELECT COUNT(*) FROM order_items;').fetchone()[0])
print("payments:", conn.execute('SELECT COUNT(*) FROM payments;').fetchone()[0])

# Close connection
conn.close()
