import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

database = "library.db"

sql_create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT NOT NULL,
                                    author TEXT NOT NULL,
                                    genre TEXT,
                                    published_year INTEGER
                                ); """

conn = create_connection(database)
if conn is not None:
    create_table(conn, sql_create_books_table)
else:
    print("Error! Cannot create the database connection.")

def add_book(conn, book):
    """ Add a new book into the books table """
    sql = ''' INSERT INTO books(title, author, genre, published_year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

def search_books(conn, query):
    """ Query books by title or author """
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%'+query+'%', '%'+query+'%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def update_book(conn, book):
    """ Update a book's details """
    sql = ''' UPDATE books
              SET title = ? ,
                  author = ? ,
                  genre = ? ,
                  published_year = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

def delete_book(conn, id):
    """ Delete a book by book id """
    sql = 'DELETE FROM books WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def main():
    database = "library.db"
    conn = create_connection(database)

    with conn:
        # Add books
        book_1 = ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925);
        add_book(conn, book_1)

        # Search for books
        print("Search results:")
        search_books(conn, "Gatsby")

        # Update a book's details
        update_book(conn, ('The Great Gatsby Revised', 'F. Scott Fitzgerald', 'Classic Fiction', 1925, 1))

        # Delete a book
        delete_book(conn, 2)


if __name__ == '__main__':
    main()
