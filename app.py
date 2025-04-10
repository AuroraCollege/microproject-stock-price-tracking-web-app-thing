#create basic app
<<<<<<< Updated upstream
from flask import Flask, request, redirect, url_for, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect, CSRFError
import sqlite3


app = Flask(__name__)
app.secret_key = 'your_secret_key'

<<<<<<< Updated upstream
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
=======
def init_db():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stocks ( StockId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, ticker TEXT NOT NULL, price TEXT NOT NULL)')
    conn.commit()
    conn.close()
>>>>>>> Stashed changes

@app.route("/layout", methods=['GET'])
def home():
    return render_template("layout.html")

@app.route("/create", methods=['GET', 'POST'])
def create_stock():

    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute("INSERT INTO stocks (name, ticker, price) VALUES (?,?,?)", (request.form.get('name')), (request.form.get('ticker')), (request.form.get('price')))
    conn.commit()
    conn.close()
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
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password) #turns password into hashed password

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        except sqlite3.Error as e:
            return "An error occurred while accessing the database.", 500
        finally:
            conn.close()

        flash('Account created successfully! Please log in.', 'success')  # Success message
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)