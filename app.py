from flask import Flask, render_template, request, redirect, url_for
from ipalib import api
from model.user import User

app = Flask(__name__)

api.bootstrap(context="cli")
api.finalize()
api.Backend.rpcclient.connect()

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/user", methods=["GET","POST"])
def new_user():
    user = User(request.form)
    errors = None
    if request.method == "POST": 
        errors = user.save()
        if not errors:
            return redirect(url_for("complete"))
    return render_template("new_user.html", user=user, errors=errors)

@app.route("/complete")
def complete():
    return render_template("complete.html")


if __name__ == "__main__":
    app.run()
