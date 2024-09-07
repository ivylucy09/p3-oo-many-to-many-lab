class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("name must be a non-empty string")
        self._name = value

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Return a list of books related to this author."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object for this author and a specified book."""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")
        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        return contract

    def total_royalties(self):
        """Return the total amount of royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Book:
    all_books = []

    def __init__(self, title):
        self._title = title
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("title must be a non-empty string")
        self._title = value

    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Return a list of authors related to this book."""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"Book(title='{self.title}')"


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int) or value < 0:
            raise Exception("royalties must be a non-negative integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date as the date passed into the method."""
        if not isinstance(date, str):
            raise Exception("date must be a string")
        # Ensure contracts are sorted by date
        return sorted([contract for contract in cls.all_contracts if contract.date == date], key=lambda c: c.royalties)

    def __repr__(self):
        return (f"Contract(author={self.author}, book={self.book}, "
                f"date='{self.date}', royalties={self.royalties})")