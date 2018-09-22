from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return 'Hello {}'.format(name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    method = request.method
    if method == 'POST':
        user = request.form['name']
    elif method == 'GET':
        user = request.args.get('name')

    return redirect(url_for('hello', name=user))


if __name__ == '__main__':
    app.run(debug= True)