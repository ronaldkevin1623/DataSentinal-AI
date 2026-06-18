from validators.date_validator import (
    validate_date
)


def validate_order_data(df):

    invalid_order_dates = 0
    invalid_date_formats = 0

    if "order_date" in df.columns:

        for value in df["order_date"]:

            if validate_date(value):
                continue

            invalid_order_dates += 1
            invalid_date_formats += 1

    return {

        "invalid_order_dates":
        invalid_order_dates,

        "invalid_date_formats":
        invalid_date_formats
    }