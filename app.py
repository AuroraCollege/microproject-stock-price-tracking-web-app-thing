#create basic app
from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/layout", methods=['GET'])
def home():
    return render_template("layout.html")

@app.route("/create", methods=['GET', 'POST'])
def create_stock():
    return render_template("create.html")

@app.route("/delete", methods=['GET', 'POST'])
def delete_stock():
    return render_template("delete.html")

@app.route("/edit", methods=['GET', 'POST'])
def edit_stock():
    return render_template("edit.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/logout", methods=['POST'])
def logout():
    return render_template("logout.html")

#app will open on register page
@app.route("/")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)