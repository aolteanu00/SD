from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def login():
    #print (request.args["username"])
    return render_template('home.html')

@app.route("/welcome")
def stuff():
    username = "alex"
    password = "pass"
    print(request.form)
    print ("????????")
    print(request.method)
    print(app)
    print(request)
    if (request.args["username"] == username) & (request.args["password"] == password):
        return render_template('welcome.html', username = request.args["username"])
    else:
        return render_template('noname.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
