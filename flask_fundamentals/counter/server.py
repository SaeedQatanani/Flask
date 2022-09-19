from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_by_route():
    session.clear()	
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['count'] += 1	
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()	
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)