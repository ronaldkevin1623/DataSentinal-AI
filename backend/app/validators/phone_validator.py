import json
import os
import pandas as pd

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "country_rules.json"
)


with open(CONFIG_PATH, "r") as f:
    COUNTRY_PHONE_RULES = json.load(f)


def validate_phone(phone, country_code):

    if pd.isna(phone) or pd.isna(country_code):
        return False

    country_code = str(country_code).upper()

    if country_code not in COUNTRY_PHONE_RULES:
        return False

    required_length = COUNTRY_PHONE_RULES[country_code]

    phone = str(phone).strip()

    return (
        phone.isdigit()
        and len(phone) == required_length
    )