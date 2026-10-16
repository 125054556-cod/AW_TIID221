<?php
    include("conexion.php");
    $conn = conexion();
    $query = "SELECT * FROM alumnos";
    $stmt = mysqli_query($conn,$query);

?>
<!DOCTYPE html>
<html>
<head>
    <title>Tabla de Alumnos</title>
</head>
<body>

    <h2>TABLA DE ALUMNOS</h2>

    <p><b>Matrícula:</b> 121039631</p>
    <p><b>Nombre:</b> Alejandra</p>
    <p><b>Apellido Paterno:</b> Briones</p>
    <p><b>Apellido Materno:</b> Patino</p>
    <p><b>Edad:</b> 30</p>
    <p><b>Acciones:</b> Eliminar</p>

</body>
</html>