from formats.account_layout import parse_fixed_record, serialize_account

RECORD_LAYOUTS = {
    "ACCOUNT": {
        "parser": parse_fixed_record,
        "serializer": serialize_account,
        "length": 68,
    }
}
