from flask import Flask, render_template

app = Flask(__name__)

@app.route('/marks/<int:score>/')
def marks(score):
    return render_template('results.html', score=score)


@app.route('/results')
def results():
    scores = { 'maths': 90, 'Eng': 80, 'Sci': 98}
    return render_template('scores.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)