# PDF Encryption Script 🔒

A simple Python utility to encrypt PDF files with a password using the **PyPDF2** library.  
This script ensures sensitive documents (like resumes or reports) are protected before sharing.


# Features
- Reads an existing PDF file
- Encrypts the PDF with a user‑defined password
- Outputs a secured version of the file
- Lightweight and easy to use


# Tech Stack
- **Language**: Python 3.x
- **Library**: [PyPDF2](https://pypi.org/project/PyPDF2/)


# Getting Started

## Prerequisites
- Python 3.8+ installed
- Install PyPDF2:
  ```bash
  pip install PyPDF2

# Usage
- Place your PDF file (e.g., ParasResume.pdf) in the project directory.
- Run the script:
python encrypt_pdf.py
- The script will:
- Read the input PDF
- Encrypt it with the password you specify in the code
- Save the encrypted file with the same name (ParasResume.pdf)
