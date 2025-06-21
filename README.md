# bank_it

Retro-Mainframe Banking System

# Features
- Fixed-width text records (COBOL-style fixed-format records)
  - 10 chars: account number
  - 20 chars: customer name
  - 10 chars: balance (in cents, zero-padded)
  - 6 chars: status
  - 8 chars: date

# Structure
bank_it/
    ├── batches/
    ├── data/
    ├── db/
    ├── formats/                 ← "Copybooks"
    │   ├── account_layout.py    ← serialize/parse logic
    │   └── transaction_layout.py
    ├── jobs/
    ├── logs/
    ├── queue/
    └── main.py
