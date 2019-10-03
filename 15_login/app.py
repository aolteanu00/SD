from flask import Flask, render_template, request
from flask import redirect
from flask import session
from flask import url_for
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)



@app.route("/")
def login():
    global entered
    entered = False
    #print (request.args["username"])
    global userw
    userw = ""
    global passw
    passw = ""
    username = "alex"
    password = "pass"

    return render_template('home.html', error = entered, passw = passw, userw = userw)

@app.route("/login")
def after():
    username = "alex"
    password = "pass"
    entered = True

    return render_template('home.html', error = entered, passw = passw, userw = userw)

@app.route("/welcome")
def stuff():
    entered = False
    username = "alex"
    password = "pass"
    print(request.form)
    print ("????????")
    print(request.method)
    print(app)
    print(request)
    userw = request.args["username"]
    passw = request.args["password"]
    session["username"] = request.args["username"]

    if (request.args["username"] == username) & (request.args["password"] == password):
        return render_template('welcome.html', username = request.args["username"], password = request.args["password"])
    else:
        return redirect(url_for('after'))


if __name__ == "__main__":
    app.debug = True
    app.run()
