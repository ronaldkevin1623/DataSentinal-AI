import pandas as pd
from datetime import datetime

from validators.phone_validator import validate_phone
from validators.order_validator import validate_order_data
from validators.product_validator import validate_product_data
from validators.payment_validator import validate_payment_data


def validate_dataset(df):

    df = df.replace(
    {
        r'^\s*$': pd.NA,
        r'^-$': pd.NA,
        'N/A': pd.NA,
        'NULL': pd.NA,
        'null': pd.NA
    },
    regex=True
    )
    print(df.isna().sum())
    total_rows = len(df)

    duplicate_rows = int(
        df.duplicated().sum()
    )

    missing_values = int(
        df.isna().sum().sum()
    )

    invalid_emails = 0
    invalid_phones = 0
    future_dates = 0
    missing_emails = 0
    missing_phones = 0

    email_pattern = (
        r'^[A-Za-z0-9._%+-]+'
        r'@[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}$'
    )

    # -----------------------------
    # Email Validation
    # -----------------------------

    if "email" in df.columns:

        missing_emails = int(
            df["email"].isna().sum()
        )

        email_series = (
            df["email"]
            .dropna()
            .astype(str)
        )

        invalid_emails = int(
            (~email_series.str.match(
                email_pattern
            )).sum()
        )

    # -----------------------------
    # Phone Validation
    # -----------------------------

    if (
        "phone_number" in df.columns
        and "country_code" in df.columns
    ):

        missing_phones = int(
        df["phone_number"].isna().sum()
    )

        invalid_phones = 0

        for _, row in df.iterrows():

            if pd.isna(row["phone_number"]):
                continue

            if not validate_phone(
                row["phone_number"],
                row["country_code"]
            ):
                invalid_phones += 1

    elif "phone_number" in df.columns:

        invalid_phones = int(
            (~df["phone_number"]
             .fillna("")
             .astype(str)
             .str.match(r'^\d{10}$'))
            .sum()
        )

    # -----------------------------
    # Future Date Validation
    # -----------------------------

    date_column = None

    if "signup_date" in df.columns:
        date_column = "signup_date"

    elif "order_date" in df.columns:
        date_column = "order_date"

    if date_column:

        dates = pd.to_datetime(
            df[date_column],
            errors="coerce",
            dayfirst=True
        )

        future_dates = int(
            (dates > datetime.now()).sum()
        )

    # -----------------------------
    # Transaction Validators
    # -----------------------------

    order_results = validate_order_data(df)

    product_results = validate_product_data(df)

    payment_results = validate_payment_data(df)

    # -----------------------------
    # Dataset Profile
    # -----------------------------

    total_columns = len(df.columns)

    numeric_columns = len(
        df.select_dtypes(
            include=["number"]
        ).columns
    )

    categorical_columns = (
        total_columns - numeric_columns
    )

    memory_usage_mb = round(
        df.memory_usage(deep=True)
        .sum()
        / (1024 * 1024),
        2
    )

    # -----------------------------
    # Column Summary
    # -----------------------------

    column_summary = []

    for col in df.columns:

        column_summary.append({

            "column": col,

            "dtype": str(
                df[col].dtype
            ),

            "missing_values": int(
                df[col].isna().sum()
            ),

            "unique_values": int(
                df[col].nunique()
            )

        })

    # -----------------------------
    # Quality Score
    # -----------------------------

    total_cells = (
        df.shape[0] * df.shape[1]
    )

    missing_percentage = (
        missing_values / total_cells * 100
        if total_cells
        else 0
    )

    duplicate_percentage = (
        duplicate_rows / total_rows * 100
        if total_rows
        else 0
    )

    validation_errors = (

    invalid_emails +

    invalid_phones +

    future_dates +

    order_results[
        "invalid_order_dates"
    ] +

    order_results[
        "invalid_date_formats"
    ] +

    product_results[
        "invalid_quantity"
    ] +

    product_results[
        "invalid_price"
    ] +

    payment_results[
        "invalid_payment_modes"
    ]

)

    validation_percentage = (

        validation_errors / total_rows * 100

        if total_rows

        else 0

    )

    quality_score = round(

        max(

            0,

            100

            - (missing_percentage * 0.5)

            - (duplicate_percentage * 0.3)

            - (validation_percentage * 0.2)

        ),

        2

    )

    # -----------------------------
    # Final Response
    # -----------------------------

    return {

        "total_rows": total_rows,

        "duplicate_rows": duplicate_rows,

        "missing_values": missing_values,

        "missing_emails": missing_emails,

        "invalid_emails": invalid_emails,

        "missing_phones": missing_phones,

        "invalid_phones": invalid_phones,

        "future_dates": future_dates,

        "quality_score": quality_score,

        **order_results,

        **product_results,

        **payment_results,

        "total_columns": total_columns,

        "numeric_columns": numeric_columns,

        "categorical_columns": categorical_columns,

        "memory_usage_mb": memory_usage_mb,

        "column_summary": column_summary

    }