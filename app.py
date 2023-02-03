# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import datetime

app = Flask(__name__)


app.secret_key = 'your secret key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test'
app.config['MYSQL_DB'] = 'cloudquicklabs'


mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		username = request.form['email']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalaccounts WHERE email = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['hospitalid']
			session['username'] = account['email']
			return render_template('masterindex.html', msg = account)
		else:
			msg = 'Incorrect username or password'
			return render_template('masterloginfail.html', msg = msg)
	return render_template('masterlogin.html')

@app.route('/')
@app.route('/stafflogin', methods =['GET', 'POST'])
def stafflogin():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'hospitalid' in request.form and 'password' in request.form:
		username = request.form['email']
		password = request.form['password']
		hospitalid = request.form['hospitalid']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalstaff WHERE email = % s AND password = % s AND hospitalid = % s', (username, password, hospitalid, ))
		account = cursor.fetchone()
		if account :
			session['loggedin'] = True
			session['id'] = account['hospitalid']
			session['staffid'] = account['staffid']
			session['staffname'] = account['staffname']
			session['role'] = account['role']
			session['username'] = account['email']
			if account['role'] == 'receptionist':
				return render_template('Receptions/receptionindex.html', msg = account)
			elif account['role'] == 'doctor':
				return render_template('Doctors/doctorindex.html', msg = account)
			elif account['role'] == 'pharmacist':
				return render_template('Pharmacist/pharmacistindex.html', msg = account)
			else :
				return render_template('StaffLogin/stafflogin.html')
		else:
			msg = 'Incorrect username or password'
			return render_template('StaffLogin/staffloginfail.html', msg = msg)
	return render_template('StaffLogin/stafflogin.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'hospitalname' in request.form and 'password' in request.form and 'ownername' in request.form and 'address' in request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form and 'phonenumber' in request.form and 'dateofsubscription' in request.form and 'pan' in request.form and 'adhaarcard' in request.form and 'gstin' in request.form:
		email = request.form['email']
		hospitalname = request.form['hospitalname']
		password = request.form['password']
		ownername = request.form['ownername']
		address = request.form['address']
		city = request.form['city']
		state = request.form['state']
		country = request.form['country']
		postalcode = request.form['postalcode']
		phonenumber = request.form['phonenumber']
		dateofsubscription = request.form['dateofsubscription']
		pan = request.form['pan']
		adhaarcard = request.form['adhaarcard']
		gstin = request.form['gstin']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalaccounts WHERE email = % s', (email, ))
		hospitalaccount = cursor.fetchone()
		if hospitalaccount:
			msg = 'Subscription already exists for email: '+email
			return render_template('masterregistersuccess.html', msg = msg)
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
			return render_template('masterregisterfailure.html', msg = msg)
		elif not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
			msg = 'Valid password has minimum 8 character with atleast one lower case ,one upper case , one digit and one special case..!!'
			return render_template('masterregisterfailure.html', msg = msg)
		else:
			cursor.execute('INSERT INTO hospitalaccounts VALUES (NULL, % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s)',(password, email, hospitalname, address, city, state, country, postalcode, ownername, phonenumber, dateofsubscription, pan, adhaarcard, gstin))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
			return render_template('masterregistersuccess.html', msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('masterregister.html', msg = msg)

@app.route('/registerstaff', methods =['GET', 'POST'])
def registerstaff():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'staffname' in request.form and 'password' in request.form and 'role' in request.form and 'specialities' in request.form and 'sex' in request.form  and 'address' in request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form and 'phonenumber' in request.form and 'dateofbirth' in request.form and 'adhaarcard' in request.form:
		email = request.form['email']
		staffname = request.form['staffname']
		password = request.form['password']
		role = request.form['role']
		specialities = request.form['specialities']
		sex = request.form['sex']
		address = request.form['address']
		city = request.form['city']
		state = request.form['state']
		country = request.form['country']
		postalcode = request.form['postalcode']
		phonenumber = request.form['phonenumber']
		dateofbirth = request.form['dateofbirth']
		adhaarcard = request.form['adhaarcard']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalstaff WHERE email = % s', (email, ))
		staffaccount = cursor.fetchone()
		if staffaccount:
			msg = 'Staff record already exists for email: '+email
			return render_template('StaffManagement/staffregistersuccess.html', msg = msg)
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
			return render_template('StaffManagement/staffregisterfailure.html', msg = msg)
		elif not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
			msg = 'Valid password has minimum 8 character with atleast one lower case ,one upper case , one digit and one special case..!!'
			return render_template('StaffManagement/staffregisterfailure.html', msg = msg)
		else:
			cursor.execute('INSERT INTO hospitalstaff VALUES (% s, NULL, % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s)',(session['id'], password, email, staffname, role, specialities, address, city, state, country, postalcode, phonenumber, dateofbirth, sex, adhaarcard))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
			return render_template('StaffManagement/staffregistersuccess.html', msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('StaffManagement/staffregister.html', msg = msg)

@app.route('/createappointment', methods =['GET', 'POST'])
def createappointment():
	msg = ''
	if request.method == 'POST' and 'patientname' in request.form and 'careof' in request.form and 'address' in request.form and 'healthissues' in request.form and 'gender' in request.form and 'age' in request.form  and 'phonenumber' in request.form and 'dateofappointment' in request.form and 'doctor' in request.form and 'specialities' in request.form and 'fees' in request.form:
		patientname = request.form['patientname']
		careof = request.form['careof']
		address = request.form['address']
		healthissues = request.form['healthissues']
		gender = request.form['gender']
		age = request.form['age']
		phonenumber = request.form['phonenumber']
		dateofappointment = request.form['dateofappointment']
		doctor = request.form['doctor']
		specialities = request.form['specialities']
		fees = request.form['fees']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO hospitalappointments VALUES (% s, NULL, % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s,  % s, % s)',(session['id'], patientname, careof, address, healthissues, gender, age,phonenumber, dateofappointment, doctor, specialities, fees))
		mysql.connection.commit()
		msg = 'You have successfully registered an appointment !'
		return render_template('Receptions/createappointmentsuccess.html', msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('Receptions/createappointment.html')

@app.route("/backtoappointment")
def backtoappointment():
	if 'loggedin' in session:
		return render_template("StaffManagement/createappointment.html")
	return redirect(url_for('login'))

@app.route("/staffupdatedisplay", methods =['GET', 'POST'])
def staffupdatedisplay():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalstaff WHERE email=% s AND hospitalid=% s', (request.form['email'], session['id'] ))
		account = cursor.fetchone()
		if account:
			return render_template("StaffManagement/staffupdatedisplay.html", account = account)
		else:
			msg = 'No staff record exist for email '+request.form['email']
			return render_template('StaffManagement/staffupdatefail.html', msg=msg)
	return redirect(url_for('login'))

@app.route("/deletestaffdata")
def deletestaffdata():
	if 'loggedin' in session:
		return render_template("StaffManagement/staffdeletemaster.html")
	return redirect(url_for('login'))

@app.route("/staffdelete", methods =['GET', 'POST'])
def staffdelete():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('DELETE FROM hospitalstaff WHERE email=% s AND hospitalid=% s', (request.form['email'], session['id'] ))
		
		try:
			mysql.connection.commit()
			msg = 'Staff record for email '+request.form['email']+' is deleted succesfully.!'
			return render_template("StaffManagement/staffdeletesuccess.html", msg=msg)
		except:
			msg = 'No staff record exist for email '+request.form['email']
			return render_template('StaffManagement/staffdeletefail.html', msg=msg)
	return redirect(url_for('login'))

@app.route("/viewallstaffdata", methods =['GET', 'POST'])
def viewallstaffdata():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalstaff WHERE hospitalid=% s', (session['id'], ))
		accounts = cursor.fetchall()
		listofaccounts = []
		for account in accounts:
			listofaccounts.append(account)
		print(listofaccounts)
		if listofaccounts:
			return render_template("StaffManagement/viewallstaffdata.html", accounts = listofaccounts)
		else:
			msg = 'No staff records exist for email: '+str(session['username'])+' and hosptial ID :'+str(session['id'])
			return render_template('StaffManagement/viewallstaffdatafail.html', msg=msg)
	return redirect(url_for('login'))

@app.route("/staffupdatedisplaymaster")
def staffupdatedisplaymaster():
	if 'loggedin' in session:
		return render_template("StaffManagement/staffupdatedisplaymaster.html")
	return redirect(url_for('login'))

@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("masterindex.html")
	return redirect(url_for('login'))

@app.route("/display")
def display():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalaccounts WHERE hospitalid = % s', (session['id'], ))
		account = cursor.fetchone()
		return render_template("masterdatadisplay.html", account = account)
	return redirect(url_for('login'))

@app.route("/displaymasterupdate")
def displaymasterupdate():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalaccounts WHERE hospitalid = % s', (session['id'], ))
		account = cursor.fetchone()
		return render_template("masterupdatedisplay.html", account = account)
	return redirect(url_for('login'))

@app.route("/adminindex")
def adminindex():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalaccounts WHERE hospitalid = % s', (session['id'], ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['hospitalid']
			session['username'] = account['email']
			return render_template('masterindex.html', msg = account)
	return redirect(url_for('login'))

@app.route("/staffindex")
def staffindex():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM hospitalstaff WHERE staffid = % s AND hospitalid = % s', (session['staffid'], session['id'], ))
		account = cursor.fetchone()
		if account :
			session['loggedin'] = True
			session['id'] = account['hospitalid']
			session['staffid'] = account['staffid']
			session['staffname'] = account['staffname']
			session['role'] = account['role']
			session['username'] = account['email']
			if account['role'] == 'receptionist':
				return render_template('Receptions/receptionindex.html', msg = account)
			elif account['role'] == 'doctor':
				return render_template('Doctors/doctorindex.html', msg = account)
			elif account['role'] == 'pharmacist':
				return render_template('Pharmacist/pharmacistindex.html', msg = account)
			else :
				return render_template('StaffLogin/stafflogin.html')
	return render_template('StaffLogin/stafflogin.html')

@app.route("/updatemasterdata", methods =['GET', 'POST'])
def updatemasterdata():
	msg = ''
	if 'loggedin' in session:
		msg = ''
		if request.method == 'POST' and 'email' in request.form and 'hospitalname' in request.form and 'password' in request.form and 'ownername' in request.form and 'address' in request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form and 'phonenumber' in request.form  and 'pan' in request.form and 'adhaarcard' in request.form and 'gstin' in request.form:
			email = request.form['email']
			hospitalname = request.form['hospitalname']
			password = request.form['password']
			ownername = request.form['ownername']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']
			postalcode = request.form['postalcode']
			phonenumber = request.form['phonenumber']
			pan = request.form['pan']
			adhaarcard = request.form['adhaarcard']
			gstin = request.form['gstin']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
				return render_template('masterupdatefail.html', msg = msg)
			elif not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
				msg = 'Valid password has minimum 8 character with atleast one lower case ,one upper case , one digit and one special case..!!'
				return render_template('masterupdatefail.html', msg = msg)
			else:
				cursor.execute('UPDATE hospitalaccounts SET password=% s,  email=% s,  hospitalname=% s,  address=% s,  city=% s,  state=% s,  country=% s,  postalcode=% s,  ownername=% s,  phonenumber=% s,  pan=% s,  adhaarcard=% s,  gstin=% s WHERE hospitalid=% s',(password, email, hospitalname, address, city, state, country, postalcode, ownername, phonenumber, pan, adhaarcard, gstin, (session['id'], )))
				mysql.connection.commit()
				msg = 'Hopsital '+hospitalname+' with ID: '+str(session['id'])+' and Email: '+email+' is updated successfully..! '
				return render_template('masterupdatesuccess.html', msg = msg)
	return redirect(url_for('login'))

@app.route("/staffdataupdate", methods =['GET', 'POST'])
def staffdataupdate():
	msg = ''
	if 'loggedin' in session:
		msg = ''
		if request.method == 'POST' and 'staffid' in request.form and 'email' in request.form and 'staffname' in request.form and 'password' in request.form and 'role' in request.form and 'specialities' in request.form and 'address' in request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form and 'phonenumber' in request.form  and 'sex' in request.form and 'adhaarcard' in request.form and 'dateofbirth' in request.form:
			staffid = request.form['staffid']
			email = request.form['email']
			staffname = request.form['staffname']
			password = request.form['password']
			role = request.form['role']
			specialities = request.form['specialities']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']
			postalcode = request.form['postalcode']
			phonenumber = request.form['phonenumber']
			dateofbirth = request.form['dateofbirth']
			adhaarcard = request.form['adhaarcard']
			gender = request.form['sex']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
				return render_template('StaffManagement/staffupdatefail.html', msg = msg)
			elif not re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', password):
				msg = 'Valid password has minimum 8 character with atleast one lower case ,one upper case , one digit and one special case..!!'
				return render_template('StaffManagement/staffupdatefail.html', msg = msg)
			else:
				cursor.execute('UPDATE hospitalstaff SET password=% s,  email=% s,  staffname=% s,  address=% s,  city=% s,  state=% s,  country=% s,  postalcode=% s,  role=% s,  phonenumber=% s,  specialities=% s,  adhaarcard=% s,  dateofbirth=% s, sex=% s WHERE hospitalid=% s AND staffid=% s ',(password, email, staffname, address, city, state, country, postalcode, role, phonenumber, specialities, adhaarcard, dateofbirth, gender, session['id'], staffid))
				mysql.connection.commit()
				msg = 'Staff '+staffname+' with ID: '+str(staffid)+' and Email: '+email+' is updated successfully..! '
				return render_template('StaffManagement/staffupdatesuccess.html', msg = msg)
	return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"))
