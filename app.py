# Libraries imports
from flask import Flask, jsonify, request
from flask_login import LoginManager

# Local imports
from models.user import User
from database import db


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

# View Login


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return jsonify({"message": "Autenticacao relizada com sucesso"}), 200

    return jsonify({"message": "Credenciais invalidas"}), 400


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
