#importando paquetes de flask
from flask import Flask, session
from flask import render_template,request,redirect,url_for
#importar funciones para generar hashes de la contraseña y comprobar
#si una contraseña coincide con el hash
from werkzeug.security import generate_password_hash,check_password_hash
from flask_mysqldb import MySQL
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
mysql = MySQL(app)

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
        password_hash = request.form["password"]
        id_rol = request.form["id_rol"]
        password_hasheada = generate_password_hash(password_hash)

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )
        if cursor.fetchone():
            cursor.close()
            return render_template(
                "login.html"
            ) 
        cursor.execute(
            """INSERT INTO usuarios
            (nombre, apaterno,amaterno,correo,password,id_rol)
            VALUES(%s,%s,%s.%s.%s,%s)""",
            (
                nombre,
                apaterno,
                amaterno,
                correo,
                password_hash,
                id_rol
            )
        )
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("home"))
    return render_template("registro")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM usuarios INNER JOIN id_rol ON usuarios.id_rol = roles.id_rol WHERE correo = %s",
            (correo,)
        )
        usuario = cursor.fetchone()
        cursor.close()
        if usuario and check_password_hash(usuario [5], password):

            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Correo o contraseña incorrectos")
    return render_template("login.html")
@app.route("/admin")
def admin():
    if "id_usuario" not in session:
        return redirect(url_for("login.html"))

    if session.get("rol") != "Administrador":
        return "acceso denegado"
    return render_template(
            "administradot.html",
            nombre = session["nombre"]
        )


        
