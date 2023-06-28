import json

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    date_make = db.Column(db.String(100), nullable=True)
    summa = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/create_film', methods=['POST', 'GET'])
def create_data():
    if request.method == 'POST':
        name = request.form['name']
        description= request.form['description']
        date_make= request.form['date_make']
        summa = request.form['summa']
        film = Film(name=name, description=description, date_make=date_make, summa=summa )
        db.session.add(film)
        db.session.commit()
        return redirect('/create_film')
        # try:
        #     db.session.add(turr)
        #     db.session.commit()
        #     return redirect('/')
        # except:
        #     return "error desoly"
    else:
        post_out = Film.query.all()
        print(type(post_out))
        dict_in = {}
        for inx, val in enumerate(post_out):
            arr = [val.name, val.description, val.date_make, val.summa]
            dict_in[inx]=arr
        print(type(dict_in))
        jsn = json.dumps(dict_in)
        return render_template('create_film.html',  post=post_out, jsn=jsn)

@app.route('/post_films')
def post():
    post_out = Film.query.all()
    return render_template('post_films.html', post=post_out)


if __name__ == "__main__":
    app.run(debug=True)