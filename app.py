import os
import time
from flask import Flask
from flask import flash, redirect, render_template, session, request
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

from helpers import apology, login_required

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configuring and giving the database
db = SQL("sqlite:///widone.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        # Ensure username was submitted
        username = request.form.get("username")
        password = request.form.get("password")
        password_conf = request.form.get("password_confarmation")

        if not username or len(db.execute("SELECT * FROM users WHERE username == ?", username)) != 0:
            return apology("username has already taken", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)
        # Ensure username_conf was submitted

        elif not password_conf or password_conf != password:
            return apology("must provide password conformation", 400)

        else:
            db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, generate_password_hash(password))
            user = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = user[0]["id"]
            return redirect("/")

@app.route("/logs")
@login_required
def log():
    # if request.method == "GET":
        
    #     return render_template("logs.html")  #change to logs.html

     #time
    named_tuple = time.localtime() # get struct_time
    log_time = time.strftime("%H:%M:%S", named_tuple)
    log_date = time.strftime("%Y-%m-%d", named_tuple)
    logs = db.execute("SELECT * FROM logs where user_id = ?", session["user_id"])
    print(logs)

    return render_template("logs.html", logs=logs, time=log_time, date=log_date)     

"""
asdljahsdlasd
First this are what you need:
log.date d
log.name d
log.duration d
time d
log.break d
log.break_duration d
"""

