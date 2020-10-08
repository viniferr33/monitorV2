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

    if request.method == "POST":

        if request.form.get('update'):
            pass

        if request.form.get('deleteNews'):
            pass

        if request.form.get('deleteWarning'):
            pass

        if request.form.get('deleteEmergency'):
            pass
        
        if request.form.get('news'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'news', title, text, date_i, date_f)

        if request.form.get('warnings'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'warnings', title, text, date_i, date_f)

        if request.form.get('emergency'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'emergency', title, text, date_i, date_f)

    emergency = fs.getAll('emergency')
    warnings = fs.getAll('warnings')
    news = fs.getAll('news')
    dis_list = getDistList()
    return render_template("monitor.html", dis_list=dis_list, news=news, emergency=emergency, warnings=warnings), 200


# # A func to get all districts from a txt # # #
def getDistList():
    districts = []
    with open('data/districts.txt', "rt") as district_list:
        for line in district_list:
            districts.append(line.rstrip("\n"))

    return districts


if __name__ == "__main__":
    app.run(debug=True)
