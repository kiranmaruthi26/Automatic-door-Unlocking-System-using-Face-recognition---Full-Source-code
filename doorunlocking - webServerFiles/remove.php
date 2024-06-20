<?php 
include 'db.php';

$id = $_GET['id'];

$query = "SELECT * FROM registeruser WHERE id=$id";
$result = mysqli_query($conn,$query);

if(mysqli_num_rows($result)>0){
	while($row = mysqli_fetch_array($result)){
		if(file_exists($row['url'])){
			unlink($row['url']);
			$del_sql = "DELETE FROM registeruser WHERE id=$id";
			if(mysqli_query($conn, $del_sql)){
				echo "1";
			}else{
				echo "0";
			}
		}
	}
}else{
	echo "-1";
}

?>