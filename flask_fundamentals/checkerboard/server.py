from flask import Flask, render_template
app = Flask(__name__)

# Each route has its own html elements.
@app.route('/')
def rigid_board(index=0):
    return render_template('index.html', currentindex = index)

@app.route('/<int:x>')
def semi_flexiable_board(index=1, x=0):
    return render_template('index.html', rows = x, currentindex = index)

@app.route('/<int:x>/<int:y>')
def flexiable_board(index=2, x=0, y=0):
    return render_template('index.html', rows = x, columns = y, currentindex = index)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def color_flexiable_board(index=3, x=0, y=0, color1 = 'red', color2 = 'black'):
    return render_template('index.html', rows = x, columns = y, firstcolor = color1, secondcolor = color2, currentindex = index)

if __name__ == '__main__':
    app.run(debug=True)
