# Hacker News Email Automation

This repository contains a Python script that automatically scrapes the latest **Hacker News Top Stories** and sends them via email. 
It uses `requests` and `BeautifulSoup` for web scraping, and Python’s `smtplib` for email delivery.

# Features
- Scrapes **Hacker News Top Stories** in real time.
- Formats stories into a clean HTML email.
- Sends automated daily updates to your inbox.
- Uses Gmail’s **App Passwords** for secure authentication.

# Prerequisites
Before running the script, ensure you have:
- **Python 3.7+** installed.
- Required Python libraries:
  bash:
  pip install requests beautifulsoup4
- A **Gmail account** with App Passwords enabled (support.google.com in Bing)
- [(bing.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.bing.com%2Fsearch%3Fq%3D%2522https%253A%252F%252Fsupport.google.com%252Faccounts%252Fanswer%252F185833%2522").
- Recipient email address(es) ready.

# Setup Instructions

1. Clone the Repository
   bash:
   git clone https://github.com/your-username/hackernews-email-automation.git
   cd hackernews-email-automation

2. Edit the Script
   Open the Python file and update the following placeholders:
   python :
   FROM = "your_email@gmail.com"
   TO = ["recipient_email@example.com"]
   PASS = "your_app_password"
   

3. Run the Script
   bash
   python hackernews_email.py

# File Structure

├── hackernews_email.py   # Main script for scraping and sending emails
└── README.md             # Documentation

# Security Notes
- Do not use your main Gmail password. Always generate and use an **App Password**.
- Keep credentials private. Do not commit sensitive information to GitHub.
- Consider using environment variables or a `.env` file for better security.
