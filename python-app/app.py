from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World!"

@app.route('/test')
def test():
    return "Hello, your in test path of DevOps World!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
