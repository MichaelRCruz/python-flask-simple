from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display():
    return "Hello, world."

@app.route('/weblog')
def weblog():
    return render_template('index.html')

app.run(debug=True, port=5000)
if __name__ == '__main__':
    app.run()
