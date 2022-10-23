#routes will be in charge of what functions are done when at an endpoint
from flask import Blueprint, jsonify
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
    

books = [
    Book(1, "A Gentle Reminder", "A gentle reminder for when you are balancing the messiness, and the beauty, of what it means to be human"),
    Book(2, "Stardust","Young Tristran Thorn will do anything to win the cold heart of beautiful Victoria—even fetch her the star they watch fall from the night sky." ),
    Book(3, "Red Sister", "It is important, when killing a nun, to ensure that you bring an army of sufficient size. For Sister Thorn of the Sweet Mercy Convent, Lano Tacsis brought two hundred men.")
]
books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods = ["GET"])
def books_library():
    books_database = []
    for book in books:
        books_database.append({"id": book.id, "Title": book.title, "description":book.description})
    return jsonify(books_database)
@books_bp.route("/<book_id>", methods = ["GET"])
def get_one_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            book_data = {"Id": book.id, "Title:":book.title,"Description":book.description}
            return book_data
    return {"message":f"book {book_id} not found"}, 404
    
