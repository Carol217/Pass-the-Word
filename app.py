#
#SoftDev1 pd7
#
#

from flask import Flask, render_template, request, session, redirect
import os #for secret key

app = Flask(__name__)

#hard coded username and password combo :(
user = "JohnSmith"
pwd = "abc123"
app.secret_key = os.urandom(32)

#assign following fxn to run when
#root route requested
@app.route("/")
def hello_world():
    if 'username' in session:
        return "welcome john"
    else:
        return render_template("login.html")

@app.route("/auth")
def authenticate():
    #print request.method
    #print request.args
    if request.args['username'] == user:
        if request.args['password'] == pwd:
            session['username'] = request.args['username']
            return redirect("/")
        else:
            return "Error: wrong password"
    else:
        return "Error: wrong username"

@app.route("/logout")
def end_session():
    session.pop('username')
    return "You have been logged out"

if __name__ == "__main__":
    app.debug = True
    app.run()
