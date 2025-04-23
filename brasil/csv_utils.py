import csv
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

CSV_PATH = Path(os.getenv("CSV_PATH"))


def look_csv():
    with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return {row["id"]: row["nome"] for row in reader}

