# Diligent A-SDLC Assignment

This repository contains:
- A prompt to generate 5 synthetic e-commerce CSV files
- A prompt to ingest the CSV files into a SQLite database
- A prompt to generate a SQL join query
- All generated datasets and scripts

The prompts follow the A-SDLC (Agent Software Development Lifecycle) approach:
clear role definition → constraints → structured data → validation.

## Structure
- /prompts → 3 prompts as required
- /scripts → ingestion script
- /sql → final join query
- /data → generated CSV files
- ecommerce.db → SQLite database created from the CSVs
