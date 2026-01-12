from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello - LAB_6 CI/CD PIPELINE 😊 V2"

app.run(host="0.0.0.0", port=8080)
