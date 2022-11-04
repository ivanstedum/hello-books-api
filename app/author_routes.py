from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.author import Author
from app.book_routes import validate_model, Book


authors_bp = Blueprint("authors", __name__,url_prefix = "/authors")


@authors_bp.route("", methods=["GET"])
def read_all_authors():

    authors = Author.query.all()
    authors_database = [author.to_dict() for author in authors]

    return jsonify(authors_database)

@authors_bp.route("", methods = ["POST"])
def create_author():

    request_body = request.get_json()
    new_author = Author.from_dict(request_body)
    if not new_author :
        return make_response("invalid Request", 400)

    db.session.add(new_author)
    db.session.commit()
    return make_response(jsonify(f"Author {new_author.name} was succesfully created"),201)

@authors_bp.route("/<author_id>/books", methods = ["POST"])
def create_book(author_id):
    author = validate_model(Author, author_id)
    request_body = request.get_json()

    new_book = Book(
        title=request_body["title"],
        description = request_body["description"],
        author=author

    )
    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} by {new_book.author.name} successfully created"), 201)

#getting all the books from an author
@authors_bp.route("/<author_id>/books", methods=["GET"])
def read_books(author_id):
    author = validate_model(Author, author_id)
    books_database=[book.to_dict() for book in author.books]
    return jsonify(books_database)