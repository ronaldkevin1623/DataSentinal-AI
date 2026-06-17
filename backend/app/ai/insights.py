def generate_insights(results):

    insights = []

    score = results["quality_score"]

    if score >= 90:
        insights.append(
            "Dataset quality is excellent."
        )

    elif score >= 75:
        insights.append(
            "Dataset quality is acceptable."
        )

    else:
        insights.append(
            "Dataset requires cleaning before analysis."
        )

    if results["duplicate_rows"] > 0:
        insights.append(
            f"{results['duplicate_rows']} duplicate rows detected."
        )

    if results["missing_values"] > 0:
        insights.append(
            f"{results['missing_values']} missing values detected."
        )

    if results["invalid_emails"] > 0:
        insights.append(
            f"{results['invalid_emails']} invalid email addresses found."
        )

    if results["invalid_phones"] > 0:
        insights.append(
            f"{results['invalid_phones']} invalid phone numbers found."
        )

    if results["future_dates"] > 0:
        insights.append(
            f"{results['future_dates']} future signup dates found."
        )

    return " ".join(insights)