from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory("web", "index.html")

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory("web", path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
