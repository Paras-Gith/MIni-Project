PDF to Audiobook Converter

This repository contains a Python script that converts any PDF document into an audiobook (MP3 file). 
It uses `PyPDF2` to extract text from PDF pages and `pyttsx3` for text‑to‑speech synthesis.

#  Features
- Extracts text from multi‑page PDF files.
- Converts text into speech using `pyttsx3`.
- Saves the output as an **MP3 audiobook**.
- Adjustable speech rate and volume.

# Prerequisites
Before running the script, ensure you have:
- Python 3.7+ installed.
- Required Python libraries:
  pip install PyPDF2 pyttsx3
  
- A PDF file (e.g., `A_Brief_Introduction_To_AI.pdf`) placed in the project directory.

# Setup Instructions

1. Clone the Repository
   git clone https://github.com/your-username/pdf-to-audiobook.git
   cd pdf-to-audiobook

2. Edit the Script
   Update the file path for your PDF and output MP3:
   
   pdf_reader = PyPDF2.PdfReader(open('A_Brief_Introduction_To_AI.pdf', 'rb'))
   output_path = r"C:\\Users\\Asus\\Desktop\\automation\\Audio_book.mp3"

4. Run the Script
   python pdf_to_audio.py

5. Check Output
   The audiobook will be saved at the specified location:
   Audiobook created successfully at: C:\Users\Asus\Desktop\automation\Audio_book.mp3

# File Structure

├── pdf_to_audio.py   # Main script for converting PDF to audiobook
├── A_Brief_Introduction_To_AI.pdf   # Example input file
└── README.md         # Documentation


# Customization

You can adjust:
# Speech Rate:  
  engine.setProperty('rate', 150)   # Default: 150 words per minute
# Volume:  
  engine.setProperty('volume', 0.9) # Range: 0.0 to 1.0


Would you like me to also **add a “Troubleshooting” section** that covers common issues like missing voices, encoding errors, or large PDF handling? That would make your README even more practical for recruiters and collaborators.
