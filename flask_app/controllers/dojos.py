from flask_app import app, render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



#! READ ALL
@app.route('/')        
def index():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos) 

#! READ ONE
@app.route('/dojo/<int:id>')
def show(id):
    data = {'id': id}
    dojo = Dojo.get_one_with_ninjas(id)
    return render_template('show.html', dojo = dojo)

#! CREATE
@app.route('/create', methods=['post'])
def new():
    Dojo.save(request.form)
    return redirect('/')




