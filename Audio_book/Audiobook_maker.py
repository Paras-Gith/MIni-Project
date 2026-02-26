import PyPDF2
import pyttsx3
import os

pdf_reader = PyPDF2.PdfReader(open('A_Brief_Introduction_To_AI.pdf', 'rb'))

engine = pyttsx3.init()


engine.setProperty('rate', 150)    
engine.setProperty('volume', 0.9)  

full_text = " "
for page_num, page in enumerate(pdf_reader.pages):
    text = page.extract_text()
    full_text += text + "\n"


output_path = r"C:\\Users\\Asus\\Desktop\\automation\Audio_book.mp3"
engine.save_to_file(full_text, output_path)
engine.runAndWait()

print("Audiobook created successfully at:", output_path)
