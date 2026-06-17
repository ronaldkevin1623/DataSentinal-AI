from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from services.audit_report import (
    generate_audit_report
)
import pandas as pd
import io

from validators.data_validator import validate_dataset
from ai.insights import generate_insights

from services.file_processor import (
    generate_cleaned_file,
    generate_error_report
)

from services.chunker import split_csv_into_chunks

from services.profiler import (
    profile_dataset
)

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    try:

        filename = file.filename.lower()

        # CSV Support
        if filename.endswith(".csv"):

            contents = await file.read()

            df = pd.read_csv(
                io.BytesIO(contents)
            )

        # Excel Support
        elif (
            filename.endswith(".xlsx")
            or filename.endswith(".xls")
        ):

            contents = await file.read()

            df = pd.read_excel(
                io.BytesIO(contents)
            )

        else:

            return {
                "error":
                "Only CSV, XLSX and XLS files are supported."
            }

        print("\n========== FILE INFO ==========")
        print("Filename:", file.filename)
        print("Rows:", len(df))
        print("Columns:", list(df.columns))
        print("===============================\n")

        # Validation
        results = validate_dataset(df)

        # Dataset Profiling
        profile = profile_dataset(df)

        # AI Insights
        insight = generate_insights(results)

        # Generate Files
        cleaned_file = generate_cleaned_file(df)

        error_report = generate_error_report(df)

        audit_report = generate_audit_report(
    {
        **results
    }
)

        # CSV Chunking
        chunk_files = split_csv_into_chunks(df)

        return {

            "filename": file.filename,

            # Validation Results
            **results,

            # Dataset Profiling
            **profile,

            # AI
            "ai_insight": insight,

            # Generated Files
            "cleaned_file": cleaned_file,
            "error_report": error_report,
            "audit_report": audit_report,
            # Chunking
            "chunks_created": len(chunk_files),
            "chunk_files": chunk_files
        }

    except Exception as e:

        print("\n========== ERROR ==========")
        print(str(e))
        print("===========================\n")

        return {
            "error": str(e)
        }


@router.get("/download/cleaned")
def download_cleaned():

    return FileResponse(
        "outputs/cleaned_output.csv",
        media_type="text/csv",
        filename="cleaned_output.csv"
    )


@router.get("/download/errors")
def download_errors():

    return FileResponse(
        "outputs/error_report.csv",
        media_type="text/csv",
        filename="error_report.csv"
    )


@router.get("/download/chunk/{chunk_id}")
def download_chunk(chunk_id: int):

    path = f"outputs/chunks/chunk_{chunk_id}.csv"

    return FileResponse(
        path,
        media_type="text/csv",
        filename=f"chunk_{chunk_id}.csv"
    )

@router.get("/download/audit")
def download_audit():

    return FileResponse(
        "outputs/audit_report.xlsx",
        media_type=(
            "application/vnd.openxmlformats-"
            "officedocument.spreadsheetml.sheet"
        ),
        filename="audit_report.xlsx"
    )