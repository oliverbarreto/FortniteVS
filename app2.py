# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, request, session, flash



## App & Config
app = Flask(__name__)



## Routes & Views
@app.route('/')
def index():
	#return render_template('index.html', players=players, vs=vs)
	return "hello world"

@app.route('/contacto')
def contacto():
	return  render_template('contacto.html')


@app.route('/politicadeprivacidad')
def politicadeprivacidad():
	return  render_template('politicadeprivacidad.html')

@app.route('/condicionesdeservicio')
def condicionesdeservicio():
	return  render_template('condicionesdeservicio.html')


## Main
if __name__ == '__main__':
  app.run(debug=True, port=5000)

