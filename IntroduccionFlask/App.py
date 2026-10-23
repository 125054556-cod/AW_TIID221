#importando paquetes de flask
from flask import Flask
from flask import render_template,request
#importar funciones para generar hashes de la contraseña y comprobar
#si una contraseña coincide con el hash
from werkzeug.security import generate_password_hash
#creamos instancia de nuestra app
app = Flask(__name__)


#configuracion de la conexion
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'dbflask'
#PERMITE QUE FLASK VUELVA A CARGAR LAS PLANTILLAS CUANDO DE MODIFICAN
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'
#creacion de ruta
@app.route("/")

def homre():
    #RETORNANDO UNA VISTA HTML DE LA CARPETA DE TEMPLATES
    return render_template("login.html")
if __name__== "__main__":
    app.run(port=5000)

@app.route("/registro", method = ["GET","POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apaterno = request.form["apaterno"]
        amaterno = request.form["amaterno"]
        correo = request.form["correo"]
        password_hash = request.form["password_hash"]
        id_rol = request.form["id_rol"]
        password_hasheada = generate_password_hash(password_hash)
        
