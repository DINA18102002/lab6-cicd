from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi - LAB_6 CI/CD PIPELINE 😊 V2 CONFIRMED"

app.run(host="0.0.0.0", port=8080)
