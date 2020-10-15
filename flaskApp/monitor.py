from app import app, fs
from flask import request, redirect, render_template, url_for, Blueprint, session
from werkzeug.security import generate_password_hash

monitor_bp = Blueprint('monitor', __name__)

# # # Monitor # # #
@app.route("/monitor", methods=["POST", "GET"])
def monitor():

    if 'user' not in session:
        return redirect(url_for('home'))

    if request.method == "POST":

        if request.form.get('logout'):
            session.pop('user', None)
            return redirect(url_for('home'))

        if request.form.get('update'):
            pass

        if request.form.get('deleteNews'):
            doc_id = request.form['deleteNews']
            fs.deleteData('news', doc_id)

        if request.form.get('deleteWarning'):
            doc_id = request.form['deleteWarning']
            fs.deleteData('warnings', doc_id)

        if request.form.get('deleteEmergency'):
            doc_id = request.form['deleteEmergency']
            fs.deleteData('emergency', doc_id)
        
        if request.form.get('deleteAdmin'):
            doc_id = request.form['deleteAdmin']
            fs.deleteData('users', doc_id)

        if request.form.get('news'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            ext_link = request.form['tl_form_link']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'news', title, text, date_i, date_f, ext_link)

        if request.form.get('warnings'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            ext_link = request.form['tl_form_link']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'warnings', title, text, date_i, date_f, ext_link)

        if request.form.get('emergency'):
            title = request.form['tl_form_title']
            text = request.form['tl_form_desc']
            location = request.form['tl_form_location']
            ext_link = request.form['tl_form_link']
            date_i = request.form['tl_form_date_i']
            date_f = request.form['tl_form_date_f']

            fs.addWarning(location, 'emergency', title, text, date_i, date_f, ext_link)
        
        if request.form.get('addAdmin'):
            email = request.form['email']
            name = request.form['name']
            password = request.form['password']
            rtPass = request.form['retype_pass']

            if fs.checkUser(email):
                ### Handle if email already exists ###
                pass
            
            else:                
                
                if password != rtPass:
                    ### Handle if password and retype password isnt the same ###
                    pass

                else:
                    fs.addUser(email, generate_password_hash(password, method='sha256'), name)
                    
            
    admin = fs.getAll('users')
    reports = fs.getAll('reports')
    emergency = fs.getAll('emergency')
    warnings = fs.getAll('warnings')
    news = fs.getAll('news')
    dis_list = getDistList()
    return render_template("monitor.html", dis_list=dis_list, news=news, emergency=emergency, warnings=warnings, reports=reports, admin=admin), 200


# # A func to get all districts from a txt # # #
def getDistList():
    districts = []
    with open('data/districts.txt', "rt") as district_list:
        for line in district_list:
            districts.append(line.rstrip("\n"))

    return districts