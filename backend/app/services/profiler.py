import pandas as pd


def profile_dataset(df):

    # Convert common missing value placeholders
    df = df.replace(
        [r'^\s*$', 'N/A', 'NULL', 'null', '-'],
        pd.NA,
        regex=True
    )

    total_columns = len(df.columns)

    numeric_columns = len(
        df.select_dtypes(
            include=["number"]
        ).columns
    )

    categorical_columns = (
        total_columns
        - numeric_columns
    )

    memory_usage_mb = round(
        df.memory_usage(
            deep=True
        ).sum()
        / (1024 * 1024),
        2
    )

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

    return {

        "total_columns": total_columns,

        "numeric_columns":
        numeric_columns,

        "categorical_columns":
        categorical_columns,

        "memory_usage_mb":
        memory_usage_mb,

        "column_summary":
        column_summary

    }