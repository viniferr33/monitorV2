from app import app, fs
from flask import request, redirect, render_template, url_for, Blueprint, session
from werkzeug.security import check_password_hash

login = Blueprint('login', __name__)

# # # Login screen # # #
@app.route("/", methods=["POST", "GET"])
def home():

    msg = ""

    if request.method == "POST":

        if request.form.get('login'):

            email = request.form['loginuser']
            password = request.form['loginpass']


            if fs.checkUser(email) and check_password_hash(fs.getUser(email)['password'], password):
                session['user'] = email
                return redirect(url_for("monitor"))

            else:
                msg = "Usuário ou senha inválidos!!"

    return render_template("login.html", msg=msg)
