from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from forms import Institution_Registration_Form, Login_Form
from flask_sqlalchemy import SQLAlchemy

web=Flask(__name__)
web.config['SECRET_KEY']='123456789'
web.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database.db"
database = SQLAlchemy()
database.init_app(web)

class Tutor(database.Model):
    id= database.Column(database.Integer, primary_key=True)
    name=database.Column(database.String(10), nullable=False)
    email=database.Column(database.String(), unique=True, nullable=False)
    password=database.Column(database.String(), nullable=False)
    hashtags=database.Column(database.String())
    img_profile=database.Column(database.String(20), nullable=False, default='default_tutor_picture.png')
    posts=database.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Tutor informations:\nId: {self.id}\nName: {self.name}\nEmail: {self.email}" 
        #return f"Tutor('Nome:{self.name}', 'Email: {self.email}')" #caso o primeiro return n funcione
    
class Pet(database.Model):
    id=database.Column(database.Integer, primary_key=True)
    name=database.Column(database.String(10), nullable=False)
    # animal_type =database.Column(database.Radio)
    breed=database.Column(database.String(15))
    age=database.Column(database.Integer)
    hashtags=database.Column(database.String)
    img_profile=database.Column(database.String(20), nullable=False, default='default_pet_picture')

    def __repr__(self):
        return f"Pet informations:\nId: {self.id}\nName: {self.name}\nage: {self.age}"
    
class Institution(database.Model):
    id=database.Column(database.Integer, primary_key=True)
    name=database.Column(database.String(10), nullable=False)
    email=database.Column(database.String(), unique=True, nullable=False)
    password=database.Column(database.String(), nullable=False)
    # focus =database.Column(database.Radio)
    description=database.Column(database.String(50))
    img_profile=database.Column(database.String(20), nullable=False, default='default_pet_picture')

    def __repr__(self):
        return f"Pet informations:\nId: {self.id}\nName: {self.name}\nage: {self.age}"

class Post(database.Model):
    id=database.Column(database.Integer, primary_key=True)
    title=database.Column(database.String(280), nullable=False)
    date_posted= database.Column(database.DateTime, nullable=False, default=datetime.today) 
    content = database.Column(database.Text, nullable=False)
    user_id= database.Column(database.Integer, database.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post informations:\nId: {self.id}\ntitle: {self.title}\ndate: {self.date_posted}"

@web.route("/")
def render_home():
    return render_template("main.html")
#criar pagina principal com login e colocar aqui
@web.route("/login", methods=['GET', 'POST'])
def render_login():
    login_form=Login_Form()
    if login_form.validate_on_submit():
        flash(f"Conta verificada para {login_form.email.data}", "sucess")
        return redirect(url_for('render_home'))
    return render_template("login.html", forms=login_form,title="Login")

@web.route("/main_register")
def render_main_register():
    return render_template("main_register_webpage.html")

@web.route("/institucion_register", methods=['GET', 'POST'])
def render_institucion_register():
    institucion_form= Institution_Registration_Form()
    if institucion_form.validate_on_submit():
        flash(f"Conta criada para {institucion_form.name.data}", "sucess")
        return redirect(url_for('render_home'))
    # if institucion_form.email.data=="":
    #     flash("campo obrigatorio")
    return render_template("organization_register.html", title="Organization", forms=institucion_form)

@web.route("/educational_resources")
def render_educational_resources():
    return render_template("educational_page.html")

if __name__=="__main__":
    web.run(debug=True)