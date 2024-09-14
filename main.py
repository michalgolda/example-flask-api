from flask import Flask
from services.greeting import GreetingService


app = Flask("example-flask-api")

@app.route("/greeting/<name>", methods=["GET"])
def greeting(name: str):
    service = GreetingService()
    service_output = service.execute(name)
    return service_output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)