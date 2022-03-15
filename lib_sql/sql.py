from re import I
import mysql.connector
from user_sql import UserSQL
from genre_sql import GenreSQL
from authors_sql import AuthorsSQL
from books_sql import BookSQL
from datetime import datetime
# db - database 
db = mysql.connector.connect(
   host="localhost",
    user="root",
    password="Abc12345!",
    db="chat",
    autocommit=True
)

cursor = db.cursor()
user_manager = UserSQL(cursor=cursor)
genre_manager = GenreSQL(cursor)
author_manager = AuthorsSQL(cursor=cursor)
book_manager = BookSQL(cursor=cursor)

for (book_id, book_name, author_id, author_name, genre_id, genre) in book_manager.get_books_full_info():
    print("book_id:", book_id)
    print("book_name:", book_name)
    print("author_id:", author_id)
    print("author_name:", author_name)
    print("genre_id:", genre_id)
    print("genre:", genre)
    print("-------------------------------------------")

cursor.close()