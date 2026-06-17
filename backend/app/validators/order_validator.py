from validators.date_validator import (
    validate_date
)


def validate_order_data(df):

    invalid_order_dates = 0

    if "order_date" in df.columns:

        for value in df["order_date"]:

            if not validate_date(value):
                invalid_order_dates += 1

    return {
        "invalid_order_dates":
        invalid_order_dates
    }