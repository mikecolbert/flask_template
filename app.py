from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('mike.html')

@app.route('/estimate')
def estimate():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)