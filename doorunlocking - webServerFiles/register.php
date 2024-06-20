<?php 
include "db.php";



header('Content-type: bitmap; charSet=utf-8');



if(isset($_POST['encode_string'])){
	$encoded_string = $_POST['encode_string'];
	$image_name  = $_POST['image_name'];
	$name = $_POST['name'];
	$age  = $_POST['age'];

	/*$encoded_string = "";
	$image_name  = "test123.jpg";
	$name = "Kiran";
	$age  = "25";*/

	$decoded_string = base64_decode($encoded_string);
	$path = 'images/'.$image_name;
	$new_filename = 'images/'.$name.'_'.rand(1000, 9999).'.jpg';

	$file = fopen($path, 'wb');

	$is_written = fwrite($file, $decoded_string);
	fclose($file);

	if($is_written>0){
		$query = "INSERT INTO registeruser(name, age, url, `datetime`) VALUES ('$name', '$age', '$new_filename', NOW())";
		rename($path, $new_filename);

		$result = mysqli_query($conn, $query);

		if($result){
			echo "Face registered Successfully";
		}else{
			echo "failed to Register Face, Please Try again";
		}

		mysqli_close($conn);
	}
}
else{
	echo "Missing Information";
}


?>