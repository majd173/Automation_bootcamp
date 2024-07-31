import argparse
from urllib import request
from flask import Flask, render_template
from object_oriented_programing.pet_management_system.src.classes.owner import Owner
from object_oriented_programing.pet_management_system.src.classes.pet import Pet

app = Flask(__name__)
store_file_path = "pet_store_management.json"

def check_positive_int(value):
    try:
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError("Year must be a positive integer")
        return int_value
    except ValueError:
        raise argparse.ArgumentTypeError("Year must be an integer")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owners')
def owners():
    return render_template('owners.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        try:
            name = request.form['name']
            if name == "":
                raise ValueError("Name cannot be empty")
            phone = request.form['phone']
            if phone < 0:
                check_positive_int()
            pets = request.form.getlist('pets')
            if pets == []:
                raise ValueError("Please select at least one pet")



            pets = request.form.getlist('pets')


        return render_template('add_owner.html')


# @app.route('/pets')
# def pets():
#     return render_template('pets.html')

# @app.route('/add_pet', methods=['GET', 'POST'])




