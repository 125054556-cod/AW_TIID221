<?php
include("conexion.php");

$id = $_POST['id'];
$nombre = $_POST['nombre'];
$apaterno = $_POST['apaterno'];
$amaterno = $_POST['amaterno'];
$edad = $_POST['edad'];
$matricula = $_POST['matricula'];

$query = "UPDATE alumnos SET nombre='$nombre', apaterno='$apaterno', amaterno='$amaterno', edad='$edad', matricula='$matricula' WHERE id='$id'";

mysqli_query($conexion, $query);

header("Location: akumnos.php");
?>