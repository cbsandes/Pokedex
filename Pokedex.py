from models.pokemon import Pokemon
from flask.globals import request
from flask import Flask, render_template
import requests
import json

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods = ["GET","post"])
def buscar():
    # try:
    pokemon = Pokemon(request.form["nome"]) # request.form["nome"] == "bulbasaur"
    pokemon.load_from_api()
    pokemon.evolve_chain()
    return render_template("buscar.html", pokemon = pokemon)

    # except:
    #     return render_template("buscar.html", pokemon = None)

if __name__ == "__main__":
    app.run(debug=True)