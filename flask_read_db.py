from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///all_orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Many_order(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id_vk = db.Column(db.Integer)
    address = db.Column(db.String(1024))

@app.route('/')
@app.route('/read_sql')
def read_sql():
    res = Many_order.query.all()
    return render_template('window_sql.html', database=res)


def add_sql(numb, id_us, address):
    try:
        order = Many_order(number=numb, id_vk=id_us, address=address)
        db.session.add(order)
        db.session.commit()
    except:
        db.session.rollback()
        print("Ошибка добавления")

db.create_all()

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)