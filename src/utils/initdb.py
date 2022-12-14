from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return

    except Exception as e:
        print(e)
        return
