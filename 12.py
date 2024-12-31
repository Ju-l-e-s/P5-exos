class Book:
    """
    A class to represent a book with a title, an author, and a publication year.

    :param title: The title of the book.
    :type title: str
    :param author: The author of the book.
    :type author: str
    :param year: The year the book was published.
    :type year: int
    """

    def __init__(self, title, author, year):
        """
        Initialize a Book object with a title, author, and publication year.

        :param title: The title of the book.
        :type title: str
        :param author: The author of the book.
        :type author: str
        :param year: The year the book was published.
        :type year: int
        """
        self.title = title
        self.author = author
        self.year = year


class Library:
    """
    A class to represent a library with a collection of books and borrowed books.

    :param books: A list of books available in the library.
    :type books: list of Book
    :param borrowed_books: A list of books that have been borrowed.
    :type borrowed_books: list of Book
    """

    def __init__(self):
        """
        Initialize a Library object with empty lists for available and borrowed books.
        """
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """
        Add a book to the library.

        :param book: The book to add.
        :type book: Book
        :return: None
        :rtype: None
        """
        self.books.append(book)

    def remove_book(self, book_title):
        """
        Remove a book from the library by its title.

        :param book_title: The title of the book to remove.
        :type book_title: str
        :return: None
        :rtype: None
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return
        print(f"Le livre '{book_title}' n'est pas dans la bibliothèque.")

    def borrow_book(self, book_title):
        """
        Borrow a book from the library by its title.

        :param book_title: The title of the book to borrow.
        :type book_title: str
        :return: None
        :rtype: None
        """
        if book_title not in self.borrowed_books:
            for book in self.books:
                if book.title == book_title:
                    self.books.remove(book)
                    self.borrowed_books.append(book)
                    return
        print(f"Le livre '{book_title}' n'est pas disponible à l'emprunt.")

    def return_book(self, book_title):
        """
        Return a borrowed book to the library by its title.

        :param book_title: The title of the book to return.
        :type book_title: str
        :return: None
        :rtype: None
        """
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return
        print(f"Le livre '{book_title}' n'a pas été emprunté ici.")

    def available_books(self):
        """
        Get a list of titles of books currently available in the library.

        :return: A list of titles of available books.
        :rtype: list of str
        """
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        """
        Get a list of titles of books currently borrowed from the library.

        :return: A list of titles of borrowed books.
        :rtype: list of str
        """
        return [book.title for book in self.borrowed_books]


# Exemple d'utilisation
library = Library()

book1 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
book2 = Book("L'Étranger", "Albert Camus", 1942)
book3 = Book("1984", "George Orwell", 1949)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Livres disponibles:", library.available_books())
library.borrow_book("1984")
print("Livres disponibles après emprunt:", library.available_books())
print("Livres empruntés:", library.borrowed_books_list())
library.return_book("1984")
print("Livres disponibles après retour:", library.available_books())
