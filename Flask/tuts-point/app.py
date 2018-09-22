from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello, this is the home page'

@app.route('/hello/')
def hello_world():
    return 'hello world'

@app.route('/admin/admin/')
def hello_admin():
    return 'hello admin'\

@app.route('/guest/<guest>/')
def hello_guest(guest):
    return 'hello {}'.format(guest)

@app.route('/hello/<name>/')
def hello_username(name):
    return 'Hello {}'.format(name)

@app.route('/user/<name>/')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))



if __name__ == '__main__':
    app.run(debug = True)