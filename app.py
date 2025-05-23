from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет! Это мой сайт на Flask, размещённый на Render.'

if __name__ == '__main__':
    app.run()