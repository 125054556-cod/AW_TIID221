<?php
include("conexion.php");

if (isset($_GET['eliminar'])) {
    $id_borrar = $_GET['eliminar'];
    mysqli_query($conexion, "DELETE FROM alumnos WHERE id = '$id_borrar'");
}

$resultado = mysqli_query($conexion, "SELECT * FROM alumnos");
?>

<!DOCTYPE html>
<html>
<body>
    <h1>Lista de Alumnos</h1>
    <a href="insertar.php">Agregar Nuevo Alumno</a>
    <br><br>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>APaterno</th>
            <th>AMaterno</th>
            <th>Edad</th>
            <th>Matricula</th>
            <th>Opciones</th>
        </tr>
        <?php while ($fila = mysqli_fetch_array($resultado)) { ?>
        <tr>
            <td><?php echo $fila['id']; ?></td>
            <td><?php echo $fila['nombre']; ?></td>
            <td><?php echo $fila['apaterno']; ?></td>
            <td><?php echo $fila['amaterno']; ?></td>
            <td><?php echo $fila['edad']; ?></td>
            <td><?php echo $fila['matricula']; ?></td>
            <td>
                <a href="delete.php?eliminar=<?php echo $fila['id']; ?>">Eliminar</a>
            </td>
        </tr>
        <?php } ?>
    </table>
</body>
</html>