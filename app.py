from flask import Flask, render_template, request, redirect, url_for
from forms import ToDo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

db = SQLAlchemy(app)


class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        return f'{self.content}, {self.id}'


@app.route('/', methods=['GET', 'POST'])
def index():
    request_method = request.method
    todo = ToDoModel.query.all()
    if request_method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return redirect(url_for('name', first_name=first_name, last_name=last_name))
    return render_template('hello.html', request_method=request_method, todo=todo)


@app.route('/name/<string:first_name> <string:last_name>')
def name(first_name, last_name):
    return f'<h1>Welcome {first_name} {last_name}</h1>'


@app.route('/<string:name>')
def greet(name):
    return f'Hello {name}'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    todo_form = ToDo()
    if todo_form.validate_on_submit():
        todo = ToDoModel(content=todo_form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo.html', form=todo_form)


if __name__ == '__main__':
    app.run(debug=True)
