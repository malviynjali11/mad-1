from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', name='Anjali')

@app.route('/submit', methods = ['POST'])
def submit():
    user_name = request.form['username']
    return render_template('greeting.html', name=user_name)

@app.route('/ssubmit', methods = ['GET','POST'])
def ssubmit():
    return render_template('greeting.html')

if __name__ == '__main__':
    app.run(debug=True)