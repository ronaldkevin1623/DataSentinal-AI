from datetime import datetime


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

    if not date_value:
        return False

    date_value = str(date_value).strip()

    for fmt in DATE_FORMATS:

        try:
            datetime.strptime(
                date_value,
                fmt
            )
            return True

        except:
            pass

    return False