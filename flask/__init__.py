from flask import Flask, render_template, request, session, redirect, url_for
from varHolder import secret_key
from firestore import FSHandler

fs = FSHandler()
app = Flask(__name__)  # Create a new Flask object
app.secret_key = secret_key

# # # Login screen # # #
@app.route("/", methods=["POST", "GET"])
def home():

    msg = ""

    if request.method == "POST":

        if request.form.get('login'):

            user = request.form['loginuser']
            password = request.form['loginpass']

            if user == "admin" and password == "mcpoze":
                session["user"] = user
                return redirect(url_for("monitor"))

            else:
                msg = "Usuário ou senha inválidos!!"

    return render_template("login.html", msg=msg)


# # # Monitor # # #
@app.route("/monitor", methods=["POST", "GET"])
def monitor():

    tldata = fs.getAll('news')
    dis_list = getDistList()
    return render_template("index.html", dis_list=dis_list, tldata=tldata), 200


# # A func to get all districts from a txt # # #
def getDistList():
    districts = []
    with open('data/districts.txt', "rt") as district_list:
        for line in district_list:
            districts.append(line.rstrip("\n"))

    return districts


if __name__ == "__main__":
    app.run(debug=True)
