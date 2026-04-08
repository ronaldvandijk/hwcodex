from flask import render_template

from models import HelloModel


class HomeController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route("/")
        def home():
            model = HelloModel(message="Hello, world!")
            return render_template(
                "index.html",
                title="Hello World App",
                model=model,
            )
