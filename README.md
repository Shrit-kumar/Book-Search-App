📚 Book Search App

A simple and beginner-friendly Python project that allows users to search for books using the Google Books API.
The app takes a book name as input and displays the title, authors, and published date for the top 5 results.

🚀 Features

Search any book by name

Fetch data from Google Books API (no API key needed)

Handles invalid or empty user input

Error handling for API failures

Clean and readable output

🛠️ Technologies Used

Python 3

Requests library

Google Books API

📦 Installation & Setup
1. Clone or download the project
git clone <your-repo-link>
cd book-search-app

2. Install required library
pip install requests

3. Run the program
python main.py

📗 How It Works

The program keeps asking the user to enter a book name.

It sends a request to:

https://www.googleapis.com/books/v1/volumes


with parameters:

q → search query

maxResults = 5

It receives JSON data, extracts:

Title

Authors

Publication date

If no results are found, the app lets the user know.

🧾 Sample Output
***Book Search App***
Type any book name to search

Search book: python

Found 5 books:

1. Learning Python
   Author(s): Mark Lutz
   Published: 2013

2. Python Crash Course
   Author(s): Eric Matthes
   Published: 2019

----------------------------
