<?php 

$host = "localhost";
$user = "root";
$password = "";
$db ="doorunlocking";
$conn = mysqli_connect($host,$user,$password,$db);

if(!$conn){
	echo "Conntection failed".mysqli_error();
}

?>