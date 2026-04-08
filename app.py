from flask import Flask

from controllers import HomeController


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")
    HomeController(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
