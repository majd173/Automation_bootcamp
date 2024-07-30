from flask import Flask, render_template
from object_oriented_programing.pet_management_system.src.classes.owner import Owner
from object_oriented_programing.pet_management_system.src.classes.pet import Pet

app = Flask(__name__)
store_file_path = "pet.store.json"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owners')
def owners():
    return render_template('owners.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner(self):
    owner = Owner.add_owner(self)
    return render_template('add_owner.html', owner=owner)


# @app.route('/pets')
# def pets():
#     return render_template('pets.html')

# @app.route('/add_pet', methods=['GET', 'POST'])




