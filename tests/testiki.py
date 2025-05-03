from flask import Flask, render_template, request
import auth


app = Flask("__main__")


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    a = auth.User()
    result = a.create_account(username, password)
    return render_template("register_result.html", result=result)


app.run(debug=True)
