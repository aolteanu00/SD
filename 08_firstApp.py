rom flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "No hablo queso!"

@app.route("apple")
def eat():
    return "yum!"

@app.route("bed")
def sleep():
    return "catch some z's"

@app.route("toothbrush")
def brush():
    return "pearly whites!"
    

if __name__ == "__main__":
    app.debug = True
    app.run()
