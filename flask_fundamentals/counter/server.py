from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/destroy', methods=['POST'])
def destroy():
    print('dsetrooooooooooooooooooooooy')
    session.clear()	
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)