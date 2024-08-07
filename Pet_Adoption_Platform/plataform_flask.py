from flask import Flask, render_template, url_for, redirect, flash
from forms import Institution_Registration_Form, Login_Form
web=Flask(__name__)

web.config['SECRET_KEY']='123456789'

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
    return render_template("organization_register.html", title="Organization", forms=institucion_form)

@web.route("/educational_resources")
def render_educational_resources():
    return render_template("educational_page.html")

if __name__=="__main__":
    web.run(debug=True)