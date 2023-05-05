import csv


def read_books(filename):
    books = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books


def search_by_author(books, author):
    result = []
    for book in books:
        if book['author'] == author:
            result.append(book)
    return result


def search_by_isbn(books, isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return book['title'], book['price']
    return None


def search_by_price_range(books, min_price, max_price):
    result = []
    for book in books:
        if min_price <= float(book['price']) <= max_price:
            result.append(book)
    return result
    
def main():
    books = read_books('booklist.csv')
    while True:
        print('Select an option:')
        print('1. Search by author')
        print('2. Search by ISBN')
        print('3. Search by price range')
        print('4. Add new book')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            author = input('Enter author name: ')
            result = search_by_author(books, author)
            if len(result) == 0:
                print('No books found')
            else:
                for book in result:
                    print(f"{book['title']} by {book['author']}, ISBN: {book['ISBN']}, Price: {book['price']}")
        elif choice == '2':
            isbn = int(input('Enter ISBN: '))
            result = search_by_isbn(books, isbn)
            if result is None:
                print('Book not found')
            else:
                title, price = result
                print(f"{title}, Price: {price}")
        elif choice == '3':
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            result = search_by_price_range(books, min_price, max_price)
            if len(result) == 0:
                print('No books found')
            else:
                for book in result:
                    print(f"{book['title']} by {book['author']}, ISBN: {book['ISBN']}, Price: {book['price']}")
        elif choice == '4':
            title = input('Enter book title: ')
            author = input('Enter author name: ')
            isbn = input('Enter ISBN: ')
            price = input('Enter price: ')
            new_book = {'title': title, 'author': author, 'ISBN': isbn, 'price': price}
            books.append(new_book)
            with open('booklist.csv', 'a', newline='') as csvfile:
                fieldnames = ['title', 'author', 'ISBN', 'price']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_book)
            print('Book added successfully')
        elif choice == '5':
            break
        else:
            print('Invalid choice')