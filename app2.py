from flask import Flask, render_template, redirect

app2 = Flask(__name__)


@app2.route("/")
@app2.route("/home")
def home():
    items = [
        {'id':1,'name':'phone','barcode':'123456789','price':10000},
        {'id':2,'name':'laptop','barcode':'45785789','price':15000},
        {'id':3,'name':'smartphone','barcode':'789456123','price':17000},
        {'id':4,'name':'tablet','barcode':'456321789','price':2000},
        {'id':5,'name':'smart-Tv','barcode':'1654895789','price':123000}
    ]
    return render_template ("home.html",items=items)


@app2.route("/login")
def login():
    return render_template("login.html")

@app2.route("/sign_up")
def sign_up():
    return render_template("sign-up.html")

@app2.route("/logout")
def logout():
    return "Success"
    redirect('/')




if __name__ == "__main__":
    app2.run(debug=True) 