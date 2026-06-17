VALID_PAYMENT_MODES = [
    "CARD",
    "UPI",
    "NETBANKING",
    "WALLET",
    "CASH"
]


def validate_payment_data(df):

    invalid_payment_modes = 0

    if "payment_mode" in df.columns:

        invalid_payment_modes = (
            ~df["payment_mode"]
            .fillna("")
            .astype(str)
            .str.upper()
            .isin(VALID_PAYMENT_MODES)
        ).sum()

    return {
        "invalid_payment_modes": int(
            invalid_payment_modes
        )
    }