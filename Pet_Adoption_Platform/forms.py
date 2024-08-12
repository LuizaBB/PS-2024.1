from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class Institution_Registration_Form(FlaskForm):
    name=StringField("organization_name", validators=[DataRequired(), Length(min=10,max=20)])
    email=StringField("organization_email", validators=[DataRequired(), Email()])
    password=PasswordField("organization_password", validators=[DataRequired(), Length(min=5,max=15)])
    focus= RadioField('Foco', choices=[('dog','Cão'),('cat','Gato')], validators=[DataRequired()])
    description= StringField("organization_description")
    submit= SubmitField("Criar conta")

class Tutor_Registration_Form(FlaskForm):
      name= StringField("Nome", validators=[DataRequired(), Length(min=3, max=10)])
      email= StringField("Email", validators=[DataRequired(), Email()])
      password= PasswordField("Password", validators=[DataRequired()])
      submit= SubmitField("Continuar")

class Pet_Registration_Form(FlaskForm):
      name= StringField("Nome do Pet", validators=[DataRequired(), Length(min=2, max=10)])
      animal= RadioField('Foco', choices=[('dog','Cão'),('cat','Gato')])
      age = IntegerField("Idade", validators=[Length(min=1, max=2)])
      breed=  StringField("Raça", validators=[Length(min=5,max=15)])
      submit= SubmitField("Cadastrar")

class Login_Form(FlaskForm):
        email= StringField("Email", validators=[DataRequired(), Email()])
        password= PasswordField("Senha", validators=[DataRequired()])
        submit= SubmitField("Entrar")