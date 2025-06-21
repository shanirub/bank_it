from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)              # Fixed width: 30 chars
    national_id = Column(String(12), unique=True, nullable=False)  # e.g., SSN, 12 digits max
    birthdate = Column(Date)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    accounts = relationship("Account", back_populates="customer")


class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    account_number = Column(String(10), unique=True, nullable=False)  # e.g., '1234567890'
    balance = Column(Integer, default=0)  # cents
    status = Column(String(10), default="active")         # e.g., 'active', 'closed'
    opened_at = Column(TIMESTAMP, default=datetime.utcnow)
    closed_at = Column(TIMESTAMP)

    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    type = Column(String(15), nullable=False)             # 'deposit', 'withdraw', etc.
    amount_cents = Column(Integer, nullable=False)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)
    description = Column(String(100))                     # optional, bounded
    batch_id = Column(Integer, ForeignKey("batches.batch_id"))

    account = relationship("Account", back_populates="transactions")
    batch = relationship("Batch", back_populates="transactions")


class Batch(Base):
    __tablename__ = "batches"
    batch_id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    status = Column(String(15), nullable=False, default="pending")
    started_at = Column(TIMESTAMP)
    finished_at = Column(TIMESTAMP)
    message = Column(Text)

    transactions = relationship("Transaction", back_populates="batch")


class MessageQueue(Base):
    __tablename__ = "message_queue"
    msg_id = Column(Integer, primary_key=True)
    payload = Column(Text, nullable=False)
    status = Column(String(10), nullable=False, default="new")
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    processed_at = Column(TIMESTAMP)


class AuditLog(Base):
    __tablename__ = "audit_log"
    log_id = Column(Integer, primary_key=True)
    event_type = Column(String(20), nullable=False)
    message = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
