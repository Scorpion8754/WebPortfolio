from flask import Flask, render_template, url_for, flash, redirect
from data import Articles
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy



application = Flask(__name__)
Articles = Articles()
application.config['SECRET_KEY'] = 'wqOOMqM1QlXYPUnH'
application.config['SQLALCHEMY_DATABASE_URI']='mysql://ShanetheMain:Barney8754!@portfoliodb.c1ubgl64fp4i.us-east-1.rds.amazonaws.com/portfoliodb'
db = SQLAlchemy(application)

@application.route('/')
def index():
    return render_template('index.html', title="Home")

@application.route('/about')
def about():
    return render_template('about.html', title="About")

@application.route('/projects')
def articles():
    return render_template('articles.html', articles = Articles, title="Projects")

@application.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

@application.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    application.run()

