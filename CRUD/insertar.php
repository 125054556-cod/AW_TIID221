<?php
include("conexion.php");
if (isset($_POST['guardar'])) {
    $nombre = $_POST['nombre'];
    $apaterno = $_POST['apaterno'];
    $amaterno = $_POST['amaterno'];
    $edad = $_POST['edad'];
    $matricula = $_POST['matricula'];
    mysqli_query($conexion, "INSERT INTO alumnos (nombre, apaterno, amaterno, edad, matricula) VALUES ('$nombre', '$apaterno', '$amaterno', '$edad', '$matricula')");
    header("Location: akumnos.php");
}
?>
<!DOCTYPE html>
<html>
<body>
    <h1>Agregar Alumno</h1>
    <form method="POST" action="insertar.php">
        Nombre: <input type="text" name="nombre"><br><br>
        APaterno: <input type="text" name="apaterno"><br><br>
        AMaterno: <input type="text" name="amaterno"><br><br>
        Edad: <input type="text" name="edad"><br><br>
        Matricula: <input type="text" name="matricula"><br><br>
        <input type="submit" name="guardar" value="Guardar">
    </form>
</body>
</html>