<?php
    
    function conexion(){
        $username = "root";
        $bdname = "aw221";
        $pwd = "";
        $servername = "localhost";
        $conn = new mysqli($servername, $username, $pwd, $bdname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        echo "Connected successfully";
        return $conn;
    }
?>   
