import telebot
from config import TOKEN
from lib_sql.user_sql import UserSQL
from lib_sql.authors_sql import AuthorsSQL
from lib_sql.genre_sql import GenreSQL
from lib_sql.books_sql import BookSQL
from telebot import types
import mysql.connector

bot = telebot.TeleBot(token=TOKEN)

db = mysql.connector.connect(
   host="localhost",
    user="root",
    password="maleekA312$",
    db="chat",
    autocommit=True
)
cursor = db.cursor()



@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    text = """
    Welcome to Ch.Aytmatov's library bot!
    """
    markup = types.InlineKeyboardMarkup()
    my_cart = types.InlineKeyboardButton("My cart", callback_data="my_cart")
    genres = types.InlineKeyboardButton("Genres", callback_data="genre")
    search = types.InlineKeyboardButton("Search", callback_data="search")
    my_books = types.InlineKeyboardButton("My books", callback_data="my_books")
    markup.row_width = 1
    markup.add(my_cart, genres, search, my_books)

    bot.send_message(message.chat.id, text=text, reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data=='genre')
def get_all_genres(call):
    message = call.message
    genre_manger = GenreSQL(cursor)
    genres = genre_manger.get_all_genres()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name) in genres:
        button = types.InlineKeyboardButton(name, callback_data=f"genre_{id}")
        markup.add(button)
    bot.edit_message_text(
        chat_id=message.chat.id, 
        text="Choose genre:",
        message_id=message.id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "my_books")
def send_user_books(call):
    message = call.message
    books_manager = BookSQL(cursor)
    books = books_manager.get_books_full_info()
    markup = types.InlineKeyboardMarkup()
    for book in books:
        name = book[1]
        book_id = book[0]
        button = types.InlineKeyboardButton(name, callback_data = f"book_{book_id}")
        markup.add(button)
    markup.row_width = 2
    bot.edit_message_text(
        chat_id = message.chat.id,
        text = "Choose book:",
        message_id = message.id,
        reply_markup = markup
    )

@bot.callback_query_handler(func=lambda call: str(call.data).startswith('book_'))
def send_book_info(call):
    message = call.message
    book_manager = BookSQL(cursor)
    book = call.data.split("_")
    book_id = book[1]
    book_data = book_manager.get_book_info(id=book_id)
    text = f"""
    Book title: {book_data[1]}
    Author: {book_data[3]}
    Genre: {book[5]}
    """
    bot.edit_message_text(
        chat_id = message.chat.id,
        text = text,
        message_id = message.id,
        reply_markup = None
    )
bot.infinity_polling()