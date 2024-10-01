# PDF Handouts Generator

This project consists of a script that generates PDF files for taking lecture notes. It creates a PDF with two outlined pages per sheet, positioned to allow note-taking around the slides. The input for this script is a PDF, typically containing slides.

## Requirements

- Python 3.x
- `PyMuPDF` library (install via `pip install PyMuPDF`)
- LaTeX distribution (e.g., TeX Live, MiKTeX) with `pdflatex` available in the system PATH

## Installation

1. Clone the repository or download the project files.
2. Ensure that you have the required libraries installed:
   ```bash
   pip install PyMuPDF
   ```
3. Make sure you have a LaTeX distribution installed on your system. You can download:
   - [TeX Live](https://www.tug.org/texlive/)
   - [MiKTeX](https://miktex.org/download)

## Usage

1. Place the PDF files you want to process into the `input` directory.
2. Run the Python script:
   ```bash
   python pdf_handouts_generator.py
   ```
3. The generated handouts will be saved in the `output` directory.

## Example

If your `input` folder contains a PDF file named `example.pdf`, the script will generate a LaTeX file and compile it into a handout PDF, saving the output as `example_handouts.pdf` in the `output` folder. Below is an example of how the output page might look like:

![output example](photos\output_example.jpg)
