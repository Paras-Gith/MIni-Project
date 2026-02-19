📚 Library Management System (LMS)
A simple command-line based Library Management System built with Python. It allows users to manage a collection of books — view, issue, return, and add books — all stored persistently in a text file.

# Features

Display Books — View all books along with their availability status
Issue Books — Issue an available book to a user with a timestamp
Return Books — Return an issued book back to the library
Add Books — Add new book titles to the library collection


# Requirements

Python 3.6+
No external libraries required (uses only built-in datetime and os modules)


📁 Project Structure
📦 library-management-system
 ┣ 📄 lms.py              # Main application file
 ┣ 📄 list_of_books.txt   # Text file storing book titles (one per line)
 ┗ 📄 README.md

# Setup & Usage
1. Clone the repository
bashgit clone https://github.com/your-username/library-management-system.git
cd library-management-system
2. Prepare the books file
Create a list_of_books.txt file in the project root and add book titles (one per line):
The Great Gatsby
To Kill a Mockingbird
1984
Harry Potter
Clean Code
3. Run the application
bashpython lms.py

# How It Works
On launch, the system loads all books from list_of_books.txt and assigns each an ID starting from 101. You'll be presented with a menu:
Press D To Display Books
Press I To Issue Books
Press A To Add books
Press R To Return Books
Press Q To Quit
Issuing a Book

Enter the Book ID when prompted
Provide your name
The book is marked as Already Issued with the date and time recorded

Returning a Book

Enter the Book ID of the book you're returning
The book status is reset to Available

Adding a Book

Enter a book title (max 25 characters)
The title is saved to list_of_books.txt and added to the current session


# Known Limitations

Book data (issue records) is not persisted between sessions — only book titles are saved to the file
Book titles are limited to 25 characters
No user authentication or multi-user support


# Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.
