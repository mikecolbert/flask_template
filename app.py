from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add', method=['POST'])
def submit_form():

    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'additional comments': request.form['additional comments']
    }

    data_list.append(data)

    return redirect('/')
