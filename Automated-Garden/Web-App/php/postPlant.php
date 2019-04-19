<?php 
    $servername = "localhost";
    $dbname = "test";
    $username = 'root';
    $password = '';
    // Create connection
    $conn = new mysqli($servername,$username, $password, $dbname);
    
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    $sql = "INSERT INTO plants (temperature, peltgen, lightstatus, 
                                plantweight, waterlevel, waterpump);
    VALUES ( rand(76, 90), rand(0, 1), 5 , 5, ,5, 5)";
    
    
?>