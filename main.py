#!/usr/bin/env python3
import sys
import os
from datetime import datetime
from docx2pdf import convert

# ====== CONFIGURATION ======
TEAM_ID = "043"  # ← Change this to your actual team ID
OUTPUT_DIR = "output"
# ===========================

def convert_docx_to_pdf(docx_path, assignment_name):
    # Validate input
    if not os.path.isfile(docx_path):
        print(f"❌ Error: File not found - {docx_path}")
        sys.exit(1)

    if not docx_path.lower().endswith(".docx"):
        print("❌ Error: Input file must be a .docx file.")
        sys.exit(1)

    # Create /output directory if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Build filename with date + team + assignment
    now = datetime.now()
    date_str = f"{now.year}-{now.month:02d}-{now.day:02d}"
    output_filename = f"{date_str}-{TEAM_ID}-{assignment_name}.pdf"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    print(f"Converting {docx_path} → {output_path} ...")

    try:
        # Convert .docx to .pdf
        convert(docx_path, output_path)
        print(f"✅ Conversion complete: {output_path}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert.py {original.docx path} {assignment_name}")
        sys.exit(1)

    docx_path = sys.argv[1]
    assignment_name = sys.argv[2]

    convert_docx_to_pdf(docx_path, assignment_name)

if __name__ == "__main__":
    main()
