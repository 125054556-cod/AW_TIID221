from flask import Flask, redirect, render_template,request,flash,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config["TEMPLATES_AUTO_REALOAD"] =True


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_peliculas'

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_peliculas')
    conPeliculas = con.fetchall()
    print(conPeliculas)
    return render_template('index.html', listPeliculas = conPeliculas)

@app.route('/editar/<int:id>')
def editar(id):
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_peliculas WHERE id=%s', (id,))
    consultarId = con.fetchone()
    con.close()
    return render_template('editarPeliculas.html' , pel = consultarId)

@app.route('/actualizar/<int:id>',methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        autor = request.form['txtAutor']
        anio = request.form['txtAnio']
        calificacion = request.form['txtCalificacion']
        resenia = request.form['txtReseña']

        con = mysql.connection.cursor()
        con.execute('UPDATE tb_peliculas SET titulo=%s, autor=%s, lanzamiento =%s,calificaCion=%s,reseña=%s WHERE id=%s', (titulo,autor,anio,calificacion,resenia,id))
        mysql.connection.commit()
    flash('SE ACTUALIZO A PELICULA' +titulo)
    return redirect(url_for('index'))



@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        autor = request.form['txtAutor']
        anio = request.form['txtAño']
        calificaion = request.form['txtCalificacion']
        resenia = request.form['txtReseña']
        print(titulo,autor,anio,calificaion,resenia)

        con = mysql.connection.cursor()
        con.execute('INSERT INTO tb_peliculas(titulo, autor, lanzamiento, calificacion, reseña) VALUES(%s,%s,%s,%s,%s)',(titulo,autor,anio,calificaion,resenia))
        mysql.connection.commit()
    flash('La pelicaula se registro correctamente')
    return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug = True)