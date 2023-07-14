from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def root():
    print(url_for('root'))
    return render_template('dist/index.html')


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='192.168.50.230', port=30000)