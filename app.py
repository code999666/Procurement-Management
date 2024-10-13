import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'procurement.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the ProcurementRequest model
class ProcurementRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    supplier = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "item_name": self.item_name,
            "supplier": self.supplier,
            "cost": self.cost,
            "description": self.description
        }

# Create the database
with app.app_context():
    db.create_all()

# Home route, display all procurement requests
@app.route('/')
def index():
    procurements = ProcurementRequest.query.all()
    return render_template('index.html', procurements=procurements)

# Form to add a new procurement request
@app.route('/add_procurement', methods=['GET'])
def add_procurement_form():
    return render_template('add_procurement.html')

# Handle the form submission for adding a new procurement request
@app.route('/add_procurement', methods=['POST'])
def add_procurement():
    item_name = request.form['item_name']
    supplier = request.form['supplier']
    cost = request.form['cost']
    description = request.form['description']

    new_request = ProcurementRequest(
        item_name=item_name,
        supplier=supplier,
        cost=cost,
        description=description
    )
    db.session.add(new_request)
    db.session.commit()
    return redirect(url_for('index'))

# Delete a procurement request
@app.route('/delete_procurement/<int:id>', methods=['POST'])
def delete_procurement(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    db.session.delete(procurement)
    db.session.commit()
    return redirect(url_for('index'))

# Display the form to edit an existing procurement request
@app.route('/edit_procurement/<int:id>', methods=['GET'])
def edit_procurement_form(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    return render_template('edit_procurement.html', procurement=procurement)

# Handle the form submission to update an existing procurement request
@app.route('/edit_procurement/<int:id>', methods=['POST'])
def edit_procurement(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    procurement.item_name = request.form['item_name']
    procurement.supplier = request.form['supplier']
    procurement.cost = request.form['cost']
    procurement.description = request.form['description']

    db.session.commit()
    return redirect(url_for('index'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
