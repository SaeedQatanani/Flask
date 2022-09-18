from flask import Flask, render_template
app = Flask(__name__)

# Each route has its own html elements.
@app.route('/')
def rigid_board():
    return render_template('index.html', rows = int(8), columns = int(8), firstcolor = 'red', secondcolor = 'black')

@app.route('/<int:x>')
def semi_flexiable_board(x=0):
    return render_template('index.html', rows = x, columns = 8, firstcolor = 'red', secondcolor = 'black')

@app.route('/<int:x>/<int:y>')
def flexiable_board(x=0, y=0):
    return render_template('index.html', rows = x, columns = y, firstcolor = 'red', secondcolor = 'black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def color_flexiable_board(x=0, y=0, color1 = 'red', color2 = 'black'):
    return render_template('index.html', rows = x, columns = y, firstcolor = color1, secondcolor = color2)

if __name__ == '__main__':
    app.run(debug=True)
