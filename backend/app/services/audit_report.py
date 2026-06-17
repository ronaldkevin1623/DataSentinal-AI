from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import os

OUTPUT_DIR = "outputs"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


def get_status(score):

    if score >= 90:
        return "EXCELLENT"

    elif score >= 75:
        return "GOOD"

    elif score >= 50:
        return "AVERAGE"

    return "POOR"


def generate_audit_report(results):

    output_path = os.path.join(
        OUTPUT_DIR,
        "audit_report.pdf"
    )

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    elements = []

    # =================================
    # TITLE
    # =================================

    elements.append(
        Paragraph(
            "DataSentinel AI",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Transaction Data Validation Audit Report",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =================================
    # EXECUTIVE SUMMARY
    # =================================

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    status = get_status(
        results["quality_score"]
    )

    summary_text = f"""
    Dataset Health Status:
    <b>{status}</b><br/><br/>

    Quality Score:
    <b>{results['quality_score']}%</b><br/><br/>

    Total Rows Analysed:
    <b>{results['total_rows']}</b>
    """

    elements.append(
        Paragraph(
            summary_text,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # =================================
    # VALIDATION RESULTS
    # =================================

    elements.append(
        Paragraph(
            "Validation Results",
            styles["Heading1"]
        )
    )

    validation_data = [

        ["Validation Type", "Count"],

        ["Duplicate Rows",
         results["duplicate_rows"]],

        ["Missing Values",
         results["missing_values"]],

        ["Invalid Emails",
         results["invalid_emails"]],

        ["Invalid Phones",
         results["invalid_phones"]],

        ["Future Dates",
         results["future_dates"]],

        ["Invalid Order Dates",
         results["invalid_order_dates"]],

        ["Invalid Quantity",
         results["invalid_quantity"]],

        ["Invalid Price",
         results["invalid_price"]],

        ["Invalid Payment Modes",
         results["invalid_payment_modes"]],

        ["Invalid Date Formats",
         results.get(
             "invalid_date_formats",
             0
         )]

    ]

    validation_table = Table(
        validation_data,
        colWidths=[250, 100]
    )

    validation_table.setStyle(
        TableStyle([

            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.HexColor("#4F46E5")),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black),

            ("FONTNAME",
             (0, 0),
             (-1, 0),
             "Helvetica-Bold")

        ])
    )

    elements.append(
        validation_table
    )

    elements.append(
        Spacer(1, 20)
    )

    # =================================
    # DATASET PROFILE
    # =================================

    elements.append(
        Paragraph(
            "Dataset Profile",
            styles["Heading1"]
        )
    )

    profile_data = [

        ["Metric", "Value"],

        ["Total Columns",
         results["total_columns"]],

        ["Numeric Columns",
         results["numeric_columns"]],

        ["Categorical Columns",
         results["categorical_columns"]],

        ["Memory Usage (MB)",
         results["memory_usage_mb"]]

    ]

    profile_table = Table(
        profile_data,
        colWidths=[250, 100]
    )

    profile_table.setStyle(
        TableStyle([

            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.HexColor("#10B981")),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black)

        ])
    )

    elements.append(
        profile_table
    )

    elements.append(
        PageBreak()
    )

    # =================================
    # COLUMN ANALYSIS
    # =================================

    elements.append(
        Paragraph(
            "Column Analysis",
            styles["Heading1"]
        )
    )

    column_data = [[

        "Column",
        "Type",
        "Missing",
        "Unique"

    ]]

    for col in results[
        "column_summary"
    ]:

        column_data.append([

            col["column"],

            col["dtype"],

            str(
                col["missing_values"]
            ),

            str(
                col["unique_values"]
            )

        ])

    column_table = Table(
        column_data
    )

    column_table.setStyle(
        TableStyle([

            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.HexColor("#F59E0B")),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black)

        ])
    )

    elements.append(
        column_table
    )

    elements.append(
        Spacer(1, 20)
    )

    # =================================
    # AI RECOMMENDATIONS
    # =================================

    elements.append(
        Paragraph(
            "AI Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = []

    if results["invalid_emails"] > 0:
        recommendations.append(
            "• Correct invalid email formats."
        )

    if results["invalid_phones"] > 0:
        recommendations.append(
            "• Verify phone numbers using country-specific validation."
        )

    if results["missing_values"] > 0:
        recommendations.append(
            "• Fill missing mandatory fields."
        )

    if results["duplicate_rows"] > 0:
        recommendations.append(
            "• Remove duplicate records before processing."
        )

    if results["future_dates"] > 0:
        recommendations.append(
            "• Review future-dated transactions."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "• No major issues detected."
        )

    for item in recommendations:

        elements.append(
            Paragraph(
                item,
                styles["BodyText"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    # =================================
    # FINAL VERDICT
    # =================================

    elements.append(
        Paragraph(
            "Final Assessment",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"""
            Overall Status:
            <b>{status}</b><br/><br/>

            Generated by:
            <b>DataSentinel AI</b><br/>

            Enterprise Data Validation Platform
            """,
            styles["BodyText"]
        )
    )

    doc.build(
        elements
    )

    return output_path