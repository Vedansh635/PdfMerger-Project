# Project-Description

# Overview
- This Python script is designed to merge multiple PDF files in a specified directory into a single PDF file. It's a convenient way to combine multiple PDFs into one document.

# Features
- Merges all PDF files in a specified directory into a single PDF file
- Supports any number of PDF files
- Easy to use: simply run the script and enter the directory path and desired merged PDF name

# How to Use
1. Clone this repository to your local machine
2. Save the `pdf_merger.py` script to a convenient location
3. Run the script from the command line or terminal or any Code Editor/IDE
4. Enter the path to the directory containing the PDF files you want to merge
5. Enter the desired name for the merged PDF file

# Example
Suppose you have a directory `pdfs` containing the following PDF files:
- `file1.pdf`
- `file2.pdf`
- `file3.pdf`
- `file4.pdf`

Running the script and entering the directory path `pdfs` and merged PDF name `merged_pdf` will create a new PDF file `merged_pdf.pdf` containing all the pages from the individual PDF files.

# Note
- This script assumes that all PDF files in the specified directory are in the same directory level.
- Make sure to test the script in a non-critical environment before running it on important PDF files.

 # Requirements
- `PyPDF2` library (install using `pip install PyPDF2`)
- `os` module (built-in Python module)

# Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
