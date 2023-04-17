from flask_app import app, render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=Dojo.get_all())

#! CREATE
@app.route('/create_ninja', methods=['post'])
def new_ninja():
    data = {'first_name': request.form['first_name'],
            'last_name': request.form['last_name'], 
            'age': request.form['age'],
            'dojo_id': request.form['dojo_id']
            }
    Ninja.save_ninja(data)
    return redirect('/')


