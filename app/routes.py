#routes will be in charge of what functions are done when at an endpoint
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.book import Book
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description
    

# books = [
#     Book(1, "A Gentle Reminder", "A gentle reminder for when you are balancing the messiness, and the beauty, of what it means to be human"),
#     Book(2, "Stardust","Young Tristran Thorn will do anything to win the cold heart of beautiful Victoria—even fetch her the star they watch fall from the night sky." ),
#     Book(3, "Red Sister", "It is important, when killing a nun, to ensure that you bring an army of sufficient size. For Sister Thorn of the Sweet Mercy Convent, Lano Tacsis brought two hundred men.")
# ]
books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods = ["POST"])
def create_books():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)
    if not new_book :
        return make_response("invalid Request", 400)
    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} succesfully created"),201)
@books_bp.route("", methods = ["GET"])
def read_all_books():
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title = title_query)
    else:
        books = Book.query.all()
    
    books_database = []
    for book in books:
        books_database.append(book.to_dict())
    return jsonify(books_database)
def validate_model(cls,model_id):
    try:
        model_id=int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__}{model_id} invalid"}, 400))
    book =  cls.query.get(model_id)
    if not book:
        abort(make_response({"message":f"{cls.__name__} {model_id} was not found"}, 404))
    return book

@books_bp.route("/<book_id>", methods =["GET"])
def get_one_book(book_id):
    book = validate_model(Book,book_id)
    return book.to_dict()

@books_bp.route("/<book_id>", methods = ["PUT"])
def update_one_book(book_id):
    book = validate_model(book_id)
    resquest_body = request.get_json()
    book.title = resquest_body["title"]
    book.description = resquest_body["description"]
    db.session.commit()
    return (make_response(jsonify({"message":f"Book {book_id} succesfully updated"}),200))

@books_bp.route("/<book_id>", methods = ["DELETE"])
def delete_one_book(book_id):
    book = validate_model(book_id)
    db.session.delete(book)
    db.session.commit()
    return (make_response(jsonify({"message": f"Book{book_id} was successfully deleted"}), 200))

# @books_bp.route("", methods = ["GET"])
# def books_library():
#     books_database = []
#     for book in books:
#         books_database.append({"id": book.id, "Title": book.title, "description":book.description})
#     return jsonify(books_database)

# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
#     for book in books:
#         if book.id == book_id:
#             return book
#     abort(make_response({"message":f"book {book_id} not found"}, 404))
# @books_bp.route("/<book_id>", methods = ["GET"])
# def get_one_book(book_id):
#     book = validate_book(book_id)
#     return json.dumps([{"Id": book.id, "Title:":book.title,"Description":book.description}])
    

    
    
