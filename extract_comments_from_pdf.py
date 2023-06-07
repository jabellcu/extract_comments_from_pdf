#!conda run -n py310 python
# coding: utf-8

import fitz  # PyMuPDF
# PyMuPDF cannot be installed through conda, only pip
from pathlib import Path
import pandas as pd
import argparse


def extract_annotations(input_file: Path) -> list:

    doc = fitz.open(input_file)

    annotations = []
    for page in doc:
        for annot in page.annots():
            info = annot.info
            colors = annot.colors
            rect = annot.rect
            highlighted_text = page.get_textbox(rect)
            annot_data = {**info, **colors}
            annot_data['highlighted_text'] = highlighted_text
            annotations.append(annot_data)

    return annotations


def extract_annotations_df(input_file) -> pd.DataFrame:
    annotations = extract_annotations(input_file)
    annotations_df = pd.DataFrame(annotations)
    return annotations_df


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Extract comments from a PDF file.')
    parser.add_argument("input_file", type=Path,
            help='Name or path to file to process.')
    parser.add_argument("-o", "--output_file", type=Path,
            help="Output file path.")
    parser.add_argument("--output_encoding",
            default='1252', type=str,
            help="Encoding to use for output file. Default: Windows' 1252.")
    parser.add_argument("-sep", "--separator",
            default='\t', type=str, dest='sep',
            help="Separator to use for output file. Default: tab")

    args = parser.parse_args()

    annotations_df = extract_annotations_df(args.input_file)

    if not args.output_file:
        args.output_file = args.input_file.with_suffix('.tsv')

    annotations_df.to_csv(args.output_file,
            encoding=args.output_encoding,
            sep=args.sep)
