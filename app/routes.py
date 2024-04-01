from app import app
from flask import render_template,redirect,url_for,flash
from app.forms import LoginForm

@app.route("/login",methods=['GET','POST'])
def index():
	form=LoginForm()

	if form.validate_on_submit():
		flash('user:{} pass: {}'.format(form.usuario.data,form.contrasenia.data))
		
		return redirect(url_for('principal'))

	return render_template("login.html",form=form)

@app.route("/prgr")
def programacion():
	return render_template("programacion.html")

@app.route("/config")
def configuracion():
	return render_template("configuracion.html")