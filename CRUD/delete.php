<?php
include("conexion.php"); 
$id_borrar = $_GET['eliminar'];
mysqli_query($conexion, "DELETE FROM alumnos WHERE id = '$id_borrar'");
header("Location: akumnos.php");
?>