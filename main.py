#!/usr/bin/env python3
import sys
import os
from datetime import datetime
import pypandoc

# ====== CONFIGURATION ======
TEAM_ID = "T42"  # ← Change this to your actual team ID
# ===========================

def convert_docx_to_pdf(docx_path, assignment_name):
    # Validate file
    if not os.path.isfile(docx_path):
        print(f"Error: File not found - {docx_path}")
        sys.exit(1)

    # Ensure file extension is .docx
    if not docx_path.lower().endswith(".docx"):
        print("Error: Input file must be a .docx file.")
        sys.exit(1)

    # Get current date for naming convention
    now = datetime.now()
    date_str = f"{now.year}-{now.month:02d}-{now.day:02d}"

    # Construct output file name
    output_filename = f"{date_str}-{TEAM_ID}-{assignment_name}.pdf"
    output_path = os.path.join(os.path.dirname(docx_path), output_filename)

    # Perform conversion
    try:
        print(f"Converting {docx_path} → {output_filename} ...")
        pypandoc.convert_file(docx_path, 'pdf', outputfile=output_path, extra_args=['--standalone'])
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
