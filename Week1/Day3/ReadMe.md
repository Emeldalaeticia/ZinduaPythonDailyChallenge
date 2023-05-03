This a program that reads in a CSV file containing information about books (title, author, ISBN, and price), and then allows the user to search for books by author, ISBN, or price range

This code defines several functions for searching and adding books to a list.

The read_books function reads a CSV file containing book information and returns a list of dictionaries representing the books.

The search_by_author function takes a list of books and an author's name as input, and returns a list of all books by that author.

The search_by_isbn function takes a list of books and an ISBN number as input, and returns the title and price of the book with that ISBN, if it exists.

The search_by_price_range function takes a list of books, a minimum price, and a maximum price as input, and returns a list of all books with prices within that range.

The main function is the main entry point for the program. It reads the CSV file and provides a menu of options to the user.

If the user selects option 1, they are prompted to enter an author's name and the program uses search_by_author to display all books by that author.

If the user selects option 2, they are prompted to enter an ISBN number and the program uses search_by_isbn to display the title and price of the book with that ISBN.

If the user selects option 3, they are prompted to enter a price range and the program uses search_by_price_range to display all books within that range.

If the user selects option 4, they are prompted to enter information about a new book, which is added to the list and written to the CSV file.

