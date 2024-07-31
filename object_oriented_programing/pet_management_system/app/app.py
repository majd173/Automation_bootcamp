import argparse
from urllib import request
from flask import Flask, render_template, redirect, url_for
from object_oriented_programing.pet_management_system.src.utilities.config_provider import ConfigProvider
from object_oriented_programing.pet_management_system.src.classes.owner import Owner
from object_oriented_programing.pet_management_system.src.classes.pet import Pet

app = Flask(__name__)
store_file_path = "../pet_store.json"
store_json = ConfigProvider().load_from_file(store_file_path)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owners')
def owners():
    return render_template('owners.html')

@app.route('/pets')
def pets():
    return render_template('pets.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        try:
            name = request.form['name']
            phone = request.form['phone']
            pets = request.form['pets']
            owner = Owner(name, phone, pets)
            store_json.add_owner(owner)
            return redirect(url_for('owners'))
        except Exception:
            raise 'Error adding an owner.'
    else:
        return render_template('add_owner.html', error=str(e))
    return render_template('add_owner.html')


@app.route('/add_pet')
def add_pet():
    if request.method == 'POST':
        try:
            name = request.form['name']
            species = request.form['species']
            age = request.form['age']
            owner = request.form['owner']
            vaccinated = request.form['vaccinated']
            pet = Pet(name, species, age, owner, vaccinated)
            store_json.add_owner(pet)
            return redirect(url_for('pets'))
        except Exception:
            raise 'Error adding a pet.'
    else:
        return render_template('pets.html', error=str(e))
    return render_template('pets.html')










