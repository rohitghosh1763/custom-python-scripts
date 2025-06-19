from docx2pdf import convert

# Convert a single file:
input_file = "Rohit Ghosh Final Report.docx"
output_file = "result.pdf"
convert(input_file, output_file)

# OR Convert all DOCX files in a folder:
# This will convert every DOCX in the directory to a PDF.
# convert("path/to/your/folder")
