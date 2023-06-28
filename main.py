from flask import Flask, render_template, request, redirect
# pip install  Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
# Создание базы через терминал python -> from main import app -> from main import db -> db.create_all()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Tures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    discription = db.Column(db.Text, nullable=True)
    # date_start = db.Column(db.DateTime, default=datetime.now)
    # date_finish = db.Column(db.DateTime, default=datetime.now)
    price = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def hello():
    mas = ['IT', 'Moskov','34afe@gmail.com','+789002039900']
    mas_cent = ['40%', '50%','70%', '30%']
    return render_template("cv.html", mas=mas, mas2=mas_cent)


@app.route('/create_data', methods=['POST', 'GET'])
def create_data():
    if request.method == 'POST':
        name = request.form['name']
        discription= request.form['discription']
        # date_start = request.form['date_start']
        # date_finish = request.form['date_finish']
        price = request.form['price']
        # turr = Tures(name=name, discription=discription, date_start=date_start, date_finish=date_finish, price=price)
        turr = Tures(name=name, discription=discription, price=price)
        db.session.add(turr)
        db.session.commit()
        return redirect('/')
        # try:
        #     db.session.add(turr)
        #     db.session.commit()
        #     return redirect('/')
        # except:
        #     return "error desoly"
    else:
        return render_template('create_data.html')

@app.route('/post')
def post():
    # post_out = Tures.query.first() получение из БВ первой записи
    post_out = Tures.query.all()

    return render_template('post.html', post=post_out)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return '<h1>Hello, World!</h1>' + "user:" + name + "-" + str(id)


if __name__ == "__main__":
    app.run(debug=True)
