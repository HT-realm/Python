from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return 'task: {0}, days til due: {1}, priority: {2}'.format(
            request.form['task'],
            request.form['duedays'],
            request.form['priority'])

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
