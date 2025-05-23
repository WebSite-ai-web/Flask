from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Привет! Это локальный сервер на 0.0.0.0'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
