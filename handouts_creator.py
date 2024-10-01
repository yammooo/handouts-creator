import os
import shutil
import fitz
import subprocess
import glob

# Function to delete all files in a directory
def cleanup_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

temp_extensions = ['*.aux', '*.tex', '*.log']
for ext in temp_extensions:
    for temp_file in glob.glob(ext):
        os.remove(temp_file)

# Create 'output' directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Cleanup all files in the 'output' directory
cleanup_directory(output_dir)

# Get list of all PDF files in the 'input' directory
input_dir = "input"
pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

# Loop over each PDF file in the 'input' folder
for pdf_file in pdf_files:
    file_name = os.path.splitext(pdf_file)[0]  # File name without extension
    pdf_path = os.path.join(input_dir, pdf_file)

    # Open the current PDF
    pdf_document = fitz.open(pdf_path)
    slide_count = len(pdf_document)

    # Prepare output file names
    output_tex_path = file_name + "_handouts.tex"
    output_pdf_path = os.path.join(output_dir, file_name + "_handouts.pdf")

    # Create LaTeX file for the current PDF
    with open(output_tex_path, "w") as file:
        file.write(r"""
\documentclass[landscape]{article}
\usepackage{pdfpages}
\usepackage[margin=0.5in]{geometry}
\usepackage{fancyhdr}
\pagestyle{empty}

\begin{document}

% Insert pages as handouts
""")

        # Loop over the pages in the PDF and add them to the LaTeX file
        i = 1
        while i <= slide_count:
            if i + 1 <= slide_count:
                file.write(f"\\includepdfmerge[fitpaper=true, nup=1x2, scale=0.8, frame, delta=0mm 7mm]{{{pdf_path.replace('\\', '/')}, {i}, {i+1}}}\n")
            else:
                file.write(f"\\includepdfmerge[fitpaper=true, nup=1x2, scale=0.8, frame, delta=0mm 7mm]{{{pdf_path.replace('\\', '/')}, {i}}}\n")
            i += 2

        # End the LaTeX document
        file.write(r"\end{document}")

    # Compile the LaTeX file into a PDF using pdflatex
    try:
        subprocess.run(["pdflatex", output_tex_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully generated {output_pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating PDF for {file_name}: {e}")

    # Move the generated PDF to the output directory
    generated_pdf = file_name + "_handouts.pdf"
    if os.path.exists(generated_pdf):
        os.rename(generated_pdf, output_pdf_path)