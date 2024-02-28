class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

    def __str__(self):
        return f"{self.title}, {self.pages} pages"

# Test the magic method
book1 = Book("Python Basics", 100)
book2 = Book("Advanced Python", 150)
combined_book = book1 + book2
print(combined_book)  # Python Basics & Advanced Python, 250 pages
