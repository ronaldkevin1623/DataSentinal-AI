import pandas as pd
import os
from validators.date_validator import validate_date
from validators.phone_validator import validate_phone

OUTPUT_DIR = "outputs"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


def generate_cleaned_file(df):

    import re
    from datetime import datetime

    cleaned_df = df.copy()

    email_pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    VALID_PAYMENT_MODES = [
        "CARD",
        "UPI",
        "NETBANKING",
        "WALLET",
        "CASH"
    ]

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()

    # Remove rows with missing values
    cleaned_df = cleaned_df.dropna()

    # -------------------------
    # Email Validation
    # -------------------------

    if "email" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["email"]
            .astype(str)
            .str.match(email_pattern)
        ]

    # -------------------------
    # Phone Validation
    # -------------------------

    if (
        "phone_number" in cleaned_df.columns
        and "country_code" in cleaned_df.columns
    ):

        cleaned_df = cleaned_df[
            cleaned_df.apply(
                lambda row:
                validate_phone(
                    row["phone_number"],
                    row["country_code"]
                ),
                axis=1
            )
        ]

    # -------------------------
    # Quantity Validation
    # -------------------------

    if "quantity" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["quantity"] > 0
        ]

    # -------------------------
    # Price Validation
    # -------------------------

    if "price" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["price"] > 0
        ]

    # -------------------------
    # Payment Validation
    # -------------------------

    if "payment_mode" in cleaned_df.columns:

        cleaned_df = cleaned_df[
            cleaned_df["payment_mode"]
            .astype(str)
            .str.upper()
            .isin(
                VALID_PAYMENT_MODES
            )
        ]

    path = os.path.join(
        OUTPUT_DIR,
        "cleaned_output.csv"
    )

    cleaned_df.to_csv(
        path,
        index=False
    )

    return path


def generate_error_report(df):

    import re
    from datetime import datetime

    errors = []

    duplicate_mask = df.duplicated()

    email_pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    VALID_PAYMENT_MODES = [
        "CARD",
        "UPI",
        "NETBANKING",
        "WALLET",
        "CASH"
    ]

    for index, row in df.iterrows():

        # -------------------------
        # Missing Values
        # -------------------------

        for column in df.columns:

            value = row[column]

            if pd.isna(value):

                errors.append({
                    "row_number": index + 1,
                    "error_type": "MISSING_VALUE",
                    "column_name": column,
                    "value": ""
                })

        # -------------------------
        # Duplicate Row
        # -------------------------

        if duplicate_mask.iloc[index]:

            errors.append({
                "row_number": index + 1,
                "error_type": "DUPLICATE_ROW",
                "column_name": "ALL",
                "value": ""
            })

        # -------------------------
        # Invalid Email
        # -------------------------

        if "email" in df.columns:

            email = str(
                row["email"]
            )

            if (
                email
                and not re.match(
                    email_pattern,
                    email
                )
            ):

                errors.append({
                    "row_number": index + 1,
                    "error_type": "INVALID_EMAIL",
                    "column_name": "email",
                    "value": email
                })

        # -------------------------
        # Invalid Phone
        # -------------------------

        if (
            "phone_number" in df.columns
            and "country_code" in df.columns
        ):

            if not validate_phone(
                row["phone_number"],
                row["country_code"]
            ):

                errors.append({
                    "row_number": index + 1,
                    "error_type": "INVALID_PHONE",
                    "column_name": "phone_number",
                    "value": row["phone_number"]
                })

        elif "phone_number" in df.columns:

            phone = str(
                row["phone_number"]
            )

            if (
                not phone.isdigit()
                or len(phone) != 10
            ):

                errors.append({
                    "row_number": index + 1,
                    "error_type": "INVALID_PHONE",
                    "column_name": "phone_number",
                    "value": phone
                })

        # -------------------------
        # Future Date
        # -------------------------

        # -------------------------
# Date Validation
# -------------------------

    date_column = None

    if "signup_date" in df.columns:
        date_column = "signup_date"

    elif "order_date" in df.columns:
        date_column = "order_date"

    if date_column:

        raw_date = str(
            row[date_column]
        )

        # Invalid Date Format

        if not validate_date(
            raw_date
        ):

            errors.append({
                "row_number": index + 1,
                "error_type": "INVALID_DATE_FORMAT",
                "column_name": date_column,
                "value": raw_date
            })

        else:

            try:

                parsed_date = pd.to_datetime(
                    raw_date,
                    dayfirst=True
                )

                if parsed_date > datetime.now():

                    errors.append({
                        "row_number": index + 1,
                        "error_type": "FUTURE_DATE",
                        "column_name": date_column,
                        "value": raw_date
                    })

            except:
                pass

        # -------------------------
        # Invalid Quantity
        # -------------------------

        if "quantity" in df.columns:

            try:

                if float(
                    row["quantity"]
                ) <= 0:

                    errors.append({
                        "row_number": index + 1,
                        "error_type": "INVALID_QUANTITY",
                        "column_name": "quantity",
                        "value": row["quantity"]
                    })

            except:
                pass

        # -------------------------
        # Invalid Price
        # -------------------------

        if "price" in df.columns:

            try:

                if float(
                    row["price"]
                ) <= 0:

                    errors.append({
                        "row_number": index + 1,
                        "error_type": "INVALID_PRICE",
                        "column_name": "price",
                        "value": row["price"]
                    })

            except:
                pass

        # -------------------------
        # Invalid Payment Mode
        # -------------------------

        if "payment_mode" in df.columns:

            payment = str(
                row["payment_mode"]
            ).upper()

            if payment not in VALID_PAYMENT_MODES:

                errors.append({
                    "row_number": index + 1,
                    "error_type": "INVALID_PAYMENT_MODE",
                    "column_name": "payment_mode",
                    "value": payment
                })

    error_df = pd.DataFrame(errors)

    path = os.path.join(
        OUTPUT_DIR,
        "error_report.csv"
    )

    error_df.to_csv(
        path,
        index=False
    )

    return path