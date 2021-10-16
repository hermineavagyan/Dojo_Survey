from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "dojo survey key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_results', methods = ['POST'])
def post_results():
    session['userName'] = request.form['name']
    session['userLocation'] = request.form['location']
    session['userLanguage'] = request.form['language']
    session['userComment'] = request.form['comments']
    return redirect('/results')
    

@app.route('/results')
def results():
    return render_template('results.html')


if __name__=="__main__":
    app.run(debug = True)