import pytest
#we need the test to connect to Flask and database
from app import create_app
from app import db
#we use @request_finished decorator to create a new database session after a request 
from flask.signals import request_finished
from app.models.book import Book
@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    # this decorator indicates that the function below will be invoked after any request is completed
    @request_finished.connect_via(app)
    #important for update request, with every request when it is finsihed, it clears out the temporary data
    def expire_session(sender, response, **extra):
        db.session.remove()
    #within the context of our app, looking at the test database, use the test database and generate new clean start to the database
    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()
    
#now we need to make a client object to act as our client
@pytest.fixture
def client(app):
    return app.test_client()

#creating 2 books
@pytest.fixture
def two_saved_books(app):
    ocean_book = Book(title="Ocean Book",
                      description="watr 4evr")
    mountain_book = Book(title="Mountain Book",
                         description="i luv 2 climb rocks")
    db.session.add_all([ocean_book, mountain_book])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()