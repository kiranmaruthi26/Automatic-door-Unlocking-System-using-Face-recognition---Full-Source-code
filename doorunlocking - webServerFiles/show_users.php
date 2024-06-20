<?php 
include 'db.php';
$query = "SELECT * FROM registeruser";
$result = mysqli_query($conn,$query);

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Door lock security registered users</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
</head>
<body>
	<div class="container bg-light mt-3 border">
		<div class="container bg-light p-2">
			<h3 class="text-warning text-center border p-2">Door Lock Securty Registered Users</h3>
		</div>
		<?php 
			if(mysqli_num_rows($result)>0){

			
			while($row = mysqli_fetch_array($result)){

		?>
		<div id="error"></div>
		<div class="border m-1">
			<div class="d-flex p-2 ustify-content-around">
				<div class="ml-3">
					<img src="<?php echo $row['url']?>" width="100">
				</div>
				<div class="ml-3">
					<h4><?php echo $row['name']?></h4>
					<h5>Age: <?php echo $row['age']?></h5>
					<!--<p>Reg on: <?php echo $row['datetime']?></p>-->
					<button class="btn btn-danger btn-sm" onclick="removeImage(<?php echo $row['id']?>)" id="<?php echo 'rm_'.$row['id']?>">Remove</button>
				</div>
			</div>

		</div>
		<?php 
			}
			}else{
				echo "<h3>No Users Found!</h3>";
			}
		?>
	</div>

	<script type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>

	<script type="text/javascript" src="./js/remove.js"></script>
</body>
</html>