from flask import Flask, render_template , redirect , url_for , flash
from forms import RegistrationForm, LoginForm 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jvuhs7d8v6t768790unsJUHY'


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods= ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("f'Account created for{form.username.data}!','success'")
        return redirect(url_for('home'))
    return render_template('register.html', title = "register" , form = form)

@app.route("/login",methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("you have been logged in", "success")
        return  redirect(url_for('home'))
    else:
        flash("login uncessfull", "danger")
    return render_template('login.html', title = "Login" , form = form)




if __name__ == "__main__":
    app.run(debug=True)