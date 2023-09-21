from PyPDF2 import PdfMerger, PdfReader
import os
import argparse
import io

parser = argparse.ArgumentParser(description="Merge all pdf in folder.")
parser.add_argument(
    "-i",
    "--input",
    type=str,
    help="The input folder.",
)

args = parser.parse_args()

dirname = args.input

filenames = os.listdir(dirname)

merger = PdfMerger()
for filename in filenames:
    merger.append(PdfReader(io.open(os.path.join(dirname, filename), "rb")))

merger.write(os.path.join(dirname, "document-output.pdf"))
