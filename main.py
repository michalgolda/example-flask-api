from flask import Flask


app = Flask("example-flask-api")

@app.route("/hello")
def hello_world():
    return {"msg": "Hello, World!"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)