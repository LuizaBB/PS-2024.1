from flask import Flask, render_template
web=Flask(__name__)

@web.route("/")
@web.route("/home")
def render_home():
    return render_template("/pagina_principal_wtlogin/mainwt_webpage.html")

@web.route("/login")
def render_login():
    return render_template("/pagina_login/login_webpage.html")
if __name__=="__main__":
    web.run(debug=True)