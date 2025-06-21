# TODO: rewrite as pytest test
from datetime import datetime

from formats.account_layout import Account, serialize_account, parse_fixed_record


def test_roundtrip():
    original = Account(
        account_number="1234567890",
        customer_name="Ada Lovelace",
        balance_cents=125000,
        status="active",
        opened_date=datetime(2024, 6, 18),
    )

    record = serialize_account(original)
    print("Serialized Record:", repr(record))

    parsed = parse_fixed_record(record)
    assert parsed == original
    print("✅ Roundtrip successful!")


if __name__ == "__main__":
    test_roundtrip()