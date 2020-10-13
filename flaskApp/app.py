from flask import Flask
from varHolder import secret_key
from firestore import FSHandler

fs = FSHandler()
app = Flask(__name__)  # Create a new Flask object
app.secret_key = secret_key