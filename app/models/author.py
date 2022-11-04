
from app import db
class Author(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates = "author")

    @classmethod
    def from_dict(cls, author_data):
        if "name" not in author_data:
            return False
        new_author = cls(name=author_data["name"])
        return new_author
    def to_dict(self):
        return dict(id = self.id, name = self.name)