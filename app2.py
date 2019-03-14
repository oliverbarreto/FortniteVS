# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, redirect, request, session, flash
from data import Articles, StoreItems


## App & Config
app = Flask(__name__)

Articulos = Articles()
Items = StoreItems()


## Routes & Views
@app.route('/')
def index():
	#return render_template('index.html', players=players, vs=vs)
	return render_template('home.html')

@app.route('/contacto')
def contacto():
	return  render_template('contacto.html')

@app.route('/privacidad')
def politicadeprivacidad():
	return  render_template('politicadeprivacidad.html')

@app.route('/condiciones')
def condicionesdeservicio():
	return  render_template('condicionesdeservicio.html')

@app.route('/clear')
def clear():
  ##session.clear()
  return redirect(url_for('index'))

@app.route('/articulos')
def articulos():
	return  render_template('articulos.html', articulos = Articulos)

@app.route('/tienda')
def articulostienda():
	return  render_template('tienda.html', items = Items)


## Main
if __name__ == '__main__':
  app.run(debug=True, port=5000)

