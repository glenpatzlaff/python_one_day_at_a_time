class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_details(self):
        return f"'{self.title}' by {self.author}, published in {self.year}."

my_favorite_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(my_favorite_book.book_details())