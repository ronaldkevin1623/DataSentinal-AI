import os
import pandas as pd


OUTPUT_FOLDER = "outputs/chunks"


def split_csv_into_chunks(df, chunk_size=200):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    chunk_files = []

    total_rows = len(df)

    for i in range(0, total_rows, chunk_size):

        chunk = df.iloc[i:i + chunk_size]

        file_path = (
            f"{OUTPUT_FOLDER}/chunk_{(i // chunk_size) + 1}.csv"
        )

        chunk.to_csv(file_path, index=False)

        chunk_files.append(file_path)

    return chunk_files