<?php
<<<<<<< HEAD
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "alumnos";

function conection(){
    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";
}
?>   
=======
$conexion = mysqli_connect("localhost", "root", "", "aw221");
?>
>>>>>>> 222a5eab803ccf6442e128e284ff859fd1c17298
