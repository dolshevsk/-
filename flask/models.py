from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cats(db.Model):
    __tablename__ = "cats"
    name = db.Column(primary_key=True)
    color = db.Column()
    tail_length = db.Column()
    whiskers_length = db.Column()


class CatColorInfo(db.Model):
    __tablename__ = "cat_color_info"
    color = db.Column(primary_key=True)
    count = db.Column()


class CatsStat(db.Model):
    __tablename__ = "cats_stat"
    tail_length_mean = db.Column(primary_key=True)
    tail_length_median = db.Column()
    tail_length_mode = db.Column()
    whiskers_length_mean = db.Column()
    whiskers_length_median = db.Column()
    whiskers_length_mode = db.Column()
