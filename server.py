from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def display():
    return "Hello, world."

@app.route('/weblog')
def weblog():
    return render_template('index.html')

@app.route('/query')
def query():
    if 'file' in request.args:
        query_filename = request.args.get('file')
        return render_template(query_filename)
    else:
        return 'nothing specified'

# http://localhost:5000/query?file=foo.html

app.run(debug=True, port=5000)
if __name__ == '__main__':
    app.run()
