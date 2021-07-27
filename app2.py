from flask import Flask, render_template, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

app2 = Flask(__name__)
app2.config['SECRET_KEY']='LongAndRandomSecretKey'


@app2.route("/")
@app2.route('/home')
def home():
    items =[
        {'id': 1,'name':'Phone', 'barcode':'08976543123','price':1000},
        {'id': 2,'name':'Laptop', 'barcode':'12345609876','price':15000},
        {'id': 3,'name':'Smartphone', 'barcode':'298347534312','price':1700},
        {'id': 4,'name':'Tablet', 'barcode':'67895422376','price':2000},
        {'id': 5,'name':'Smart-TV', 'barcode':'983452309','price':2345000}
    ]
    return render_template("Home.html", items=items)

@app2.route("/sign_up")
def sign_up():
    return render_template("Sign-up.html")

@app2.route("/login")
def login():
    return render_template("login.html")

@app2.route("/logout")
def logout():
    return "Success"
    redirect('/')

@app2.route('/register', methods =["GET", "POST"])
def register():

    class CreateUserForm(FlaskForm):
        
        username = StringField(label=('Username'), 
            validators=[DataRequired(), 
            Length(max=64)])
        email = StringField(label=('Email'), 
            validators=[DataRequired(), 
            Email(), 
            Length(max=120)])
        password = PasswordField(label=('Password'), 
            validators=[DataRequired(), 
            Length(min=8, message='Password should be at least %(min)d characters long')])
        confirm_password = PasswordField(
            label=('Confirm Password'), 
            validators=[DataRequired(message='*Required'),
            EqualTo('password', message='Both password fields must be equal!')])

        receive_emails = BooleanField(label=('Receive merketting emails.'))

        submit = SubmitField(label=('Submit'))
    form =CreateUserForm()
    return render_template('registration.html', form=form)

if __name__ == "__main__":
    app2.run(debug=True)