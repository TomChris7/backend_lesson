from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask import request


class MyForm(FlaskForm):
    name = EmailField('Email', validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Must be more than 6 characters")])
    submit = SubmitField(label='Log in')




app = Flask(__name__)

app.secret_key = "secret something"
csrf = CSRFProtect(app)

req_u_name = "admin@email.com"
req_password = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    # form.validate_on_submit()
    if form.validate_on_submit():
        if form.name.data == req_u_name and form.password.data == req_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")


    #
    #     print(form.name.data)
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
