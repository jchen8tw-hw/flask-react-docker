from flask import Flask, send_from_directory, request, send_file, jsonify, make_response


app = Flask(__name__, static_folder='build', static_url_path='/static')


@app.get("/api/hello")
def hello():
    return {"hello": "world"}


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
