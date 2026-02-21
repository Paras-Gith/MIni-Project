Internship Application Email Automation
This repository contains a Python script that automates sending internship application emails to HR, including a personalized message and an attached resume. It leverages Python’s built-in smtplib and email libraries to securely send emails via Gmail.

 Features
- Automates sending internship application emails.
- Attaches your resume file to the email.
- Uses Gmail’s App Passwords for secure authentication.
- Customizable subject line and body content.

 Prerequisites
Before running the script, ensure you have:
- Python 3.7+ installed.
- A Gmail account with App Passwords enabled (support.google.com in Bing).
- Your resume file saved locally (e.g., resume.pdf).

 Setup Instructions
- Clone the Repository
git clone https://github.com/your-username/internship-email-automation.git
cd internship-email-automation
- Edit the Script Open the Python file and update the following placeholders:
sender_email = "your_email@gmail.com"
reciver_email = "hr_email@example.com"
password = "your_app_password"
filename = "resume.pdf"
- Customize the Email Content Modify the subject and body variables to match your application details:
subject = "Application for Internship"
body = """Dear Hiring Manager,
I am excited to apply for a Data Engineering internship...
Best regards,
Paras Nainwal
nainwalparas@gmail.com"""
- Run the Script
python send_email.py

 File Structure
.
├── send_email.py   # Main script for sending emails
├── resume.pdf      # Your resume file (replace with your own)
└── README.md       # Documentation

 Security Notes
- Do not use your main Gmail password. Always generate and use an App Password.
- Keep your credentials private. Do not commit sensitive information to GitHub.
- Consider using environment variables or a .env file for better security
