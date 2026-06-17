import pandas as pd


def validate_product_data(df):

    invalid_quantity = 0
    invalid_price = 0

    if "quantity" in df.columns:

        qty = pd.to_numeric(
            df["quantity"],
            errors="coerce"
        )

        invalid_quantity = int(
            qty.isna().sum()
            + (qty <= 0).sum()
        )

    if "price" in df.columns:

        price = pd.to_numeric(
            df["price"],
            errors="coerce"
        )

        invalid_price = int(
            price.isna().sum()
            + (price <= 0).sum()
        )

    return {
        "invalid_quantity": invalid_quantity,
        "invalid_price": invalid_price
    }