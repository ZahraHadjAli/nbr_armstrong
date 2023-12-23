from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, World!'
    return '<strong>Bienvenu dans notre mini projet Armstrong .. <br> <br> HADJ ALI Zahra <br> <br> MAGHRAOUI Farah  </strong> '

if __name__ == '__main__':
    app.run(debug=True, port=8080)
