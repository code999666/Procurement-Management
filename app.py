import os
from flask import Flask, request,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'procurement.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 定义采购请求模型
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

# 创建数据库
with app.app_context():
    db.create_all()

# 首页，显示所有采购请求
@app.route('/')
def index():
    procurements = ProcurementRequest.query.all()
    return render_template('index.html', procurements=procurements)

# 添加采购请求的表单页面
@app.route('/add_procurement', methods=['GET'])
def add_procurement_form():
    return render_template('add_procurement.html')

# 处理添加采购请求
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

@app.route('/delete_procurement/<int:id>', methods=['POST'])
def delete_procurement(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    db.session.delete(procurement)
    db.session.commit()
    return redirect(url_for('index'))

# Display the form to edit an existing procurement
@app.route('/edit_procurement/<int:id>', methods=['GET'])
def edit_procurement_form(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    return render_template('edit_procurement.html', procurement=procurement)

# Handle the form submission to update the procurement
@app.route('/edit_procurement/<int:id>', methods=['POST'])
def edit_procurement(id):
    procurement = ProcurementRequest.query.get_or_404(id)
    procurement.item_name = request.form['item_name']
    procurement.supplier = request.form['supplier']
    procurement.cost = request.form['cost']
    procurement.description = request.form['description']

    db.session.commit()
    return redirect(url_for('index'))


# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True)