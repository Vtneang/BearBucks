from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<cur_user>')
def account(cur_user):
	file = open("data.json")
	data = json.load(file)["userdata"][cur_user]
	name = data["Name"]
	email = data["Email"]
	return render_template('account.html', User=cur_user, Name=name, Email=email, data=data["Transactions"])

@app.route('/<cur_user>/logout')
def logout(cur_user):
	return render_template('logout.html', User=cur_user)

@app.route('/<cur_user>/overview')
def overview(cur_user):
	file = open('data.json')
	data = json.load(file)
	return render_template('overview.html', User=cur_user, data=data["userdata"][cur_user]["Transactions"])

@app.route('/login', methods = ["GET", "POST"])
def login():
	if request.method == "POST":
		user = request.form['user']
		password = request.form['password']
		user_data = {}
		file = open("data.json")
		data = json.load(file)
		if user in data["emails"]:
			user_by_email = data["emails"][user]
			user_data = data["userdata"][user_by_email]
		elif user in data["userdata"]:
			user_data = data["userdata"][user]
		else:
			# Make sure to implement a error msg popup on redirection
			file.close()
			return redirect(request.url)
		file.close()
		if user_data["Password"] == password:
			x = overview(user)
			return x
		else:
			# Make sure to implement a error msg popup on redirection
			return redirect(request.url)
	return render_template('login.html')

@app.route('/signup', methods = ["GET", "POST"])
def signup():
	if request.method == "POST":
		new_name = request.form['name']
		new_email = request.form['email']
		new_user = request.form['username']
		new_pass = request.form['password']
		if new_pass == "" or new_user == "" or new_name == "" or new_email == "":
			# Make sure to implement a error msg popup on redirection
			return redirect(request.url)
		file = open("data.json")
		data = json.load(file)
		if new_email in data["emails"] or new_user in data["userdata"]:
			# Throw an error or something
			return redirect(request.url)
		data["emails"][new_email] = new_user
		data["userdata"][new_user] = {"Name": new_name, "Email": new_email, "Username": new_user, "Password": new_pass, "Transactions":[]}
		file.close()
		new_file = open("data.json", "w")
		json.dump(data, new_file, indent="")
		new_file.close()
		x = overview(new_user)
		return x
	return render_template('signup.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contactus')
def contactus():
	return render_template('contact.html')

@app.route('/<cur_user>/edit')
def edit(cur_user):
	file = open('data.json')
	data = json.load(file)
	return render_template('edit.html', User=cur_user, data=data["userdata"][cur_user]["Transactions"])

@app.route('/<cur_user>/input', methods = ["GET", "POST"])
def input(cur_user):
	file = open('data.json')
	data = json.load(file)
	return render_template('input.html', User=cur_user, data=data["userdata"][cur_user]["Transactions"])


if __name__ == '__main__':
	app.run()