from PyPDF2 import PdfWriter, PdfReader

writer = PdfWriter()
reader = PdfReader("ParasResume.pdf")
for page in reader.pages:
    writer.add_page(page)
writer.encrypt('Password')
with open(f'ParasResume.pdf', 'wb') as output_file:
    writer.write(output_file)
print('PDF encrypted')
