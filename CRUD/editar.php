<?php
include("conexion.php");
$id = $_GET['id'];
$consulta = mysqli_query($conexion, "SELECT * FROM alumnos WHERE id='$id'");
$fila = mysqli_fetch_array($consulta);
?>

<!DOCTYPE html>
<html>
<body>
    <h1>Editar Alumno</h1>
    <form method="POST" action="update.php">        
        <input type="hidden" name="id" value="<?php echo $fila['id']; ?>">
        Nombre: <input type="text" name="nombre" value="<?php echo $fila['nombre']; ?>"><br><br>
        A. Paterno: <input type="text" name="apaterno" value="<?php echo $fila['apaterno']; ?>"><br><br>
        A. Materno: <input type="text" name="amaterno" value="<?php echo $fila['amaterno']; ?>"><br><br>
        Edad: <input type="text" name="edad" value="<?php echo $fila['edad']; ?>"><br><br>
        Matrícula: <input type="text" name="matricula" value="<?php echo $fila['matricula']; ?>"><br><br>
        <input type="submit" value="Guardar Cambios">
    </form>
    <br>
    <a href="akumnos.php">Cancelar</a>
</body>
</html>