from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controllers import HomeController

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    HomeController(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)

