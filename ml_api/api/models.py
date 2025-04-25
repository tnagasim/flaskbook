from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()


class ImageInfo(db.Model):  # type: ignore
    # テーブル定義
    __tablename__ = "image_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_id = db.Column(db.String)
    filename = db.Column(db.String)

    def __repr__(self):
        return f"<Filename {self.filename}>"
