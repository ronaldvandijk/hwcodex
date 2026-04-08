from flask import render_template, request, redirect, url_for

from models import HelloModel, Message
from app import db


class HomeController:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                email = request.form.get("email")
                message_text = request.form.get("message")
                if first_name and last_name and email and message_text:
                    msg = Message(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        message=message_text
                    )
                    db.session.add(msg)
                    db.session.commit()
                return redirect(url_for("home"))

            model = HelloModel(message="Hello, world!")
            messages = Message.query.all()
            return render_template(
                "index.html",
                title="Hello World App",
                model=model,
                messages=messages,
            )


