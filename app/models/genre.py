from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    
    @classmethod
    def from_dict(cls, genre_data):
        if "name" not in genre_data:
            return False
        new_genre = Genre(name=genre_data["name"])
        return new_genre

    def to_dict(self):
        book_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
        if self.author:
            book_dict["author"] = self.author.name

        if self.genres:
            genre_names = [genre.name for genre in self.genres]
            book_dict["genres"] = genre_names

        return book_dict



    