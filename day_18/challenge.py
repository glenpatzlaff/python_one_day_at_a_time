from functools import reduce

# Defining the list of books
books = [
    {"title": "Python Tricks", "author": "Dan Bader", "pages": 302},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "pages": 792},
    {"title": "Learning Python", "author": "Mark Lutz", "pages": 1648},
    {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "pages": 504},
    {"title": "Effective Python", "author": "Brett Slatkin", "pages": 227}
]

# Filter books with more than 300 pages
books_over_300_pages = filter(lambda x: x['pages'] > 300, books)

# Map to extract titles of the selected books
titles = map(lambda x: x['title'], books_over_300_pages)

# Reduce to concatenate titles into a single string, separated by semicolons
titles_concatenated = reduce(lambda x, y: x + ';' + y, titles)

print(titles_concatenated)
