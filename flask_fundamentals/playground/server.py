from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/play')
# def three_boxes():
#     return render_template('index.html')

# @app.route('/play/<int:x>')
# def user_boxes(x):
#     return render_template('sndindex.html', repeats=x)

# @app.route('/play/<int:x>/<color>')
# def user_boxes_colored(x, color):
#     return render_template('thirdindex.html', repeats=x, mycolor=color)

@app.route('/play')
def three_boxes(temp=0):
    return render_template('bouns.html', mytemp=temp)

@app.route('/play/<int:x>')
def user_boxes(x, temp=1):
    return render_template('bouns.html', repeats=x, mytemp=temp)

@app.route('/play/<int:x>/<color>')
def user_boxes_colored(x, color, temp=2):
    return render_template('bouns.html', repeats=x, mycolor=color, mytemp=temp)

if __name__ == '__main__':
    app.run(debug=True)
