from formats.account_layout import parse_fixed_record
from db.models import Account, Customer, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/bank.db")
Base.metadata.create_all(engine)

def process_batch(file_path):
    with open(file_path, "r") as f, Session(engine) as session:
        for line in f:
            record = parse_fixed_record(line)
            # Create DB objects (simplified)
            customer = Customer(name=record.customer_name, national_id="000000000000")
            session.add(customer)
            session.flush()  # To get customer_id
            account = Account(
                customer_id=customer.customer_id,
                account_number=record.account_number,
                balance=record.balance_cents,
                status=record.status,
            )
            session.add(account)
        session.commit()

process_batch("batches/batch_001.txt")
