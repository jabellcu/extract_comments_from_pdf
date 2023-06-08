# Introduction

_extract_comments_from_pdf.py_ is a tool to output comments (annotations) from a
pdf file into a table that can be opened with your favorite spreadsheet
software.

![Alt text](https://github.com/jabellcu/extract_comments_from_pdf/blob/main/Example.png)

# Requirements

You will need python (at least 3.10) and PyMuPDF. I haven't been able to
install PyMuPDF with conda, so just use pip:

    python -m pip install PyMuPDF

# Usage

Pretty straightforward:

    >>> python extract_comments_from_pdf.py file_name

It will output _file_name.tsv_. To find other options:

    >>> pyton extract_comments_from_pdf.py -h

# Disclaimer

Use at yout own risk! The author doesn't accept any responisbility over and is
not liable for any damage caused by execution of this code and/or any modified
version of it.
