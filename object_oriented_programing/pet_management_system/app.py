import argparse
import logging  # Error handling and recording adding/editing/removing a book.
from flask import Flask, render_template, request, redirect, url_for
from pet import Pet

app = Flask(__name__)
pet_file_path = 'pets.json'
pet = Pet.load_store(pet_file_path)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owners')
def owners():
    return render_template('owners.html')

@app.route('/add_owner', methods=['GET', 'POST'])


@app.route('/pets')
def pets():
    return render_template('pets.html')

# @app.route('/add_pet', methods=['GET', 'POST'])




