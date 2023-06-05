import os

from flask import Flask
from flask import flash, redirect, render_template, session, request
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

from helpers import apology, login_required

app = Flask(__name__)
