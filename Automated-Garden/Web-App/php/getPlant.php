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

$sql = "SELECT * FROM plants ORDER BY ID DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
	
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo(json_encode($row));
    }
} else {
    echo "null";
}
$conn->close();
?>