from flask import Flask, render_template, request, session, redirect, url_for
from varHolder import secret_key
from firestore import FSHandler

app = Flask(__name__)           #Create a new Flask object
app.secret_key = secret_key


if __name__ == "__main__":
    app.run(debug=True)