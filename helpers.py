from flask import Flask
from flask import flash, redirect, render_template, session, request
from flask_session import Session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

class Log:
    def __init__(self):
        self.name = request.form.get("log-name")
        self.dur = request.form.get("log-duration")
        self.userid = session["user_id"]

        if request.form.get("log-break"):
            self.lbreak = True
        else :
            self.lbreak = False
        if self.lbreak:
            self.breakdur = request.form.get("log-break-duration")
        else:
            self.breakdur = None
        
    def me(self):
        print(self.name)
        print(self.dur)
        print(self.lbreak)
        print(self.breakdur)
    
