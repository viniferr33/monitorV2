from app import app
from flask import request, redirect, render_template, url_for

# # # Login screen # # #
@app.route("/", methods=["POST", "GET"])
def home():

    msg = ""

    if request.method == "POST":

        if request.form.get('login'):

            user = request.form['loginuser']
            password = request.form['loginpass']

            if user == "admin" and password == "mcpoze":
                return redirect(url_for("monitor"))

            else:
                msg = "Usuário ou senha inválidos!!"

    return render_template("login.html", msg=msg)