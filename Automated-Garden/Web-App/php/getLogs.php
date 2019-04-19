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

$sql = "SELECT * FROM plants ORDER BY ID DESC LIMIT 100";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    $rows = array();
	
    while($row = $result->fetch_assoc()) {
        array_push($rows, $row);
    }
    echo(json_encode($rows));	
} else {
    echo "null";
}
$conn->close();
?>