from datetime import datetime
import pandas as pd


DATE_FORMATS = [

    "%d/%m/%Y",
    "%m/%d/%Y",
    "%Y-%m-%d",

    "%d-%m-%Y",
    "%Y/%m/%d",

    "%d/%m/%Y %H:%M:%S",
    "%Y-%m-%d %H:%M:%S"
]


def validate_date(date_value):

    if pd.isna(date_value):
        return False

    # Handle already parsed datetime objects
    if isinstance(date_value, (datetime, pd.Timestamp)):
        return True

    date_value = str(date_value).strip()

    if date_value == "":
        return False

    for fmt in DATE_FORMATS:

        try:
            datetime.strptime(
                date_value,
                fmt
            )
            return True

        except ValueError:
            continue

    return False