from flask import Flask
app = Flask(__name__)

@app.route("/")
def homre():
    return "hooal flask soy obed"
if __name__== "__main__":
    app.run(port=5000)