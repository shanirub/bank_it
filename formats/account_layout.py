# serialize / parse account logic

from datetime import datetime
from dataclasses import dataclass


@dataclass
class Account:
    account_number: str
    customer_name: str
    balance_cents: int
    status: str
    opened_date: datetime


def serialize_account(account: Account) -> str:
    return (
        f"{account.account_number:<10}"         # left-aligned, pad spaces
        f"{account.customer_name:<30}"
        f"{account.balance_cents:010d}"         # zero-padded
        f"{account.status:<10}"
        f"{account.opened_date.strftime('%Y%m%d')}"
    )


def parse_fixed_record(record: str) -> Account:
    return Account(
        account_number=record[0:10].strip(),
        customer_name=record[10:40].strip(),
        balance_cents=int(record[40:50]),
        status=record[50:60].strip(),
        opened_date=datetime.strptime(record[60:68], "%Y%m%d"),
    )
