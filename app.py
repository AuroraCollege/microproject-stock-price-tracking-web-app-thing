#create basic app
from flask import Flask

app = Flask(__name__)
app.route("/")

def home():
    return render_template("layout.html")


def create_stock():
    return render_template("create.html")

def delete_stock():
    return render_template("delete.html")

def edit_stock():
    return render_template("edit.html")

def login():
    return render_template("login.html")

def logout():
    return render_template("logout.html")

def register():
    return render_template("register.html")
