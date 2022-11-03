
from app import db
#by default, SQLAlchemy will use whatever you named the class as lowercased, so lower case book will be our table
class Book(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", back_populates = "books")
    #if for some reason you didnt like default table name you can specift a different name saying __tablename__ = whatver
    @classmethod
    def from_dict(cls, book_data):
        if "title" not in book_data or "description" not in book_data:
            return False
        new_book = Book(title=book_data["title"],
                    description=book_data["description"])
        return new_book
    def to_dict(self):
        return dict(id = self.id, title = self.title, description = self.description)

    