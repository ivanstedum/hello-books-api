from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.book import Book
from app.models.author import Author
from app.models.genre import Genre


genre_bp = Blueprint("genre", __name__, url_prefix="/genre")
def validate_model(cls,model_id):
    try:
        model_id=int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__}{model_id} invalid"}, 400))
    model =  cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} was not found"}, 404))
    return model
@genre_bp.route("", methods=["GET"])
def read_all_genre():

    genres = Genre.query.all()
    genres_database = [genre.to_dict() for genre in genres]

    return jsonify(genres_database)

@genre_bp.route("", methods = ["POST"])
def create_genre():

    request_body = request.get_json()
    new_genre = Genre.from_dict(request_body)
    if not new_genre :
        return make_response("invalid Request", 400)

    db.session.add(new_genre)
    db.session.commit()
    return make_response(jsonify(f"Genre {new_genre.name} was succesfully created"),201)

@genre_bp.route("/<genre_id>/books", methods=["POST"])
def add_a_genre_to_a_book(genre_id):
    genre =  validate_model(Genre, genre_id)
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author_id=request_body["author_id"],
        genres=[genre]
    )
    db.session.add(new_book)
    db.session.commit()
    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)

@genre_bp.route("/<genre_id>/books", methods=["GET"])
def read_all_books(genre_id):
    
    genre = validate_model(Genre, genre_id)

    books_response = []
    for book in genre.books:
        books_response.append(
            book.to_dict()
        )
    return jsonify(books_response)