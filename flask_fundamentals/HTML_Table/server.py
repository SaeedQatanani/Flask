from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users')
def render_lists():
    users_info = [
        {'first_name' : 'Saeed', 'last_name': 'Qatanani'},
        {'first_name' : 'Sameer', 'last_name': 'Khalil'},
        {'first_name' : 'Abd', 'last_name': 'Mahmoud'},
        {'first_name' : 'Hussen', 'last_name': 'Osama'},
    ]
    return render_template('index.html', users = users_info)

if __name__ == '__main__':
    app.run(debug=True)