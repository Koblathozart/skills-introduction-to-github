from pypdf import PdfReader, PdfWriter
import os

# Full path to your page PDF
input_pdf_path ="C:\\Users\\Emmanuel Agbovie\\Downloads\\ACCRA EAST\\BILLS\\LEGON\\work-LEGON\\ad89f2c0-decb-4682-81ae-ded1d052a337_1"

# Directory where the single-page PDFs will be saved
output_dir = "C:\\Users\\Emmanuel Agbovie\\Desktop\\PYTHON\\pdf_single"
os.makedirs(output_dir, exist_ok=True)

# Load the original PDF
reader = PdfReader(input_pdf_path)

# Loop through each page and write to a new single-page PDF
for i in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[i])

    output_path = os.path.join(output_dir, f"page_{i + 1}.pdf")
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Saved: {output_path}")
0