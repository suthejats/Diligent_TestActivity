# Diligent Test Activity: Synthetic E-Commerce Dataset

This repository contains a complete synthetic e-commerce dataset generation project, demonstrating AI prompting skills, data engineering, and SQL querying capabilities.

## 📁 Project Structure

```
.
├── prompts/
│   ├── generate_data_prompt.txt    # Prompt for generating synthetic data
│   ├── ingest_data_prompt.txt      # Prompt for creating ingestion script
│   ├── join_query_prompt.txt       # Prompt for SQL join query
│   └── validation_prompt.txt       # Bonus: Data validation prompt
├── data/
│   ├── users.csv                   # User data (150 rows)
│   ├── products.csv                # Product catalog (50 rows)
│   ├── orders.csv                  # Order records (350 rows)
│   ├── order_items.csv             # Order line items (700 rows)
│   └── payments.csv                # Payment transactions (350 rows)
├── scripts/
│   └── ingest.py                   # Python script to load CSVs into SQLite
├── sql/
│   └── join_query.sql              # SQL query joining all tables
├── ecommerce.db                    # SQLite database (generated)
└── README.md                       # This file
```

## 🚀 How to Run

### Prerequisites
- Python 3.x
- pandas (`pip install pandas`)
- sqlite3 (built-in with Python)

### 1. Ingest Data into Database
```bash
python scripts/ingest.py
```

Expected output:
```
Inserted 150 rows into users
Inserted 50 rows into products
Inserted 350 rows into orders
Inserted 700 rows into order_items
Inserted 350 rows into payments
```

### 2. Run the SQL Query
```bash
sqlite3 ecommerce.db < sql/join_query.sql
```

This will output a table of successful orders with user details, product info, and payment data.

## 📊 Dataset Overview

- **Users**: 150 synthetic users with realistic names, emails, and signup dates
- **Products**: 50 items across Electronics, Clothing, and Books categories
- **Orders**: 350 orders with various statuses (delivered, shipped, cancelled, returned)
- **Order Items**: 700 line items linking orders to products with quantities and prices
- **Payments**: 350 payment records with methods (card, UPI, COD) and success/failure status

## 🎯 Key Features

- **Relational Integrity**: All foreign keys are valid, no orphaned records
- **Realistic Data**: Dates clustered around human behavior patterns, prices reflecting market psychology
- **AI-Generated**: Entire dataset created using structured prompts to AI agents
- **Production-Ready**: Clean, consistent data suitable for testing and analytics

## 🤖 AI Prompting Showcase

This project demonstrates advanced AI prompting techniques:
- **DataSmith-47**: Synthetic data generation with constraints
- **Ingestor-X**: Code generation for data pipelines
- **QueryMaestro**: Complex SQL query composition
- **AuditBot-9**: Data validation and integrity checks

Each prompt is designed to elicit specific, high-quality outputs from AI systems.

## 📈 Use Cases

- E-commerce analytics testing
- Data pipeline development
- SQL query optimization
- AI prompting best practices demonstration

---

**Repository**: [https://github.com/suthejats/Diligent_TestActivity](https://github.com/suthejats/Diligent_TestActivity)
