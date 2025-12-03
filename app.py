from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuario quemado para prueba
USERS = {
    "admin": "1234"
}

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in USERS and USERS[username] == password:
        return redirect(url_for("home"))

    return render_template("login.html", error="Credenciales incorrectas")

@app.route("/home")
def home():
    return render_template("home.html")
