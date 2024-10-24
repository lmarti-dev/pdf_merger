from PyPDF2 import PdfWriter, PdfReader
import os
import io
import fire
from pathlib import Path


def merge_pdfs(dirname: str, filename: str = "document-output", password: str = None):

    pdf_files = os.listdir(dirname)

    merger = PdfWriter()
    for pdf_file in pdf_files:
        if pdf_file.endswith(".pdf"):
            merger.append(PdfReader(io.open(Path(dirname, pdf_file), "rb")))
        else:
            print(f"Skipping {pdf_file}")

    if password is not None:
        merger.encrypt(user_password=password, owner_password=password)

    if not filename.endswith(".pdf"):
        filename += ".pdf"

    fpath_out = Path(dirname, filename)
    merger.write(fpath_out)

    print(f"Wrote {fpath_out}")


if __name__ == "__main__":
    fire.Fire(merge_pdfs)
