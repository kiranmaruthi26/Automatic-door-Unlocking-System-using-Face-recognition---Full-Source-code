<?php 
include "db.php";
header('Content-type: bitmap; charSet=utf-8');

$query = "SELECT * FROM registeruser";
$result = mysqli_query($conn,$query);

while($row = mysqli_fetch_assoc($result)){
	$data[] = $row;
}

print(json_encode($data));

mysqli_close($conn)


?>