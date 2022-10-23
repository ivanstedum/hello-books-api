# so this __init__ file is where we set up all stuff flask
from flask import Flask

def create_app(test_config = None):
    app = Flask(__name__)
    from .routes import books_bp
    app.register_blueprint(books_bp)
    return app