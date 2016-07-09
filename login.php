<?php
##########################################################################
$password = "okoun";  // Modify Password to suit for access, Max 10 Char.
##########################################################################
?>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link type="text/css" rel="stylesheet" href="new.css" />
    <?php 
        session_start();
    ?>	
</head>

<body>
<div class="container">
<form action="login.php" method="post">
Username: <input type="text" size="10" name="username" value=""/> <br>
<input type="submit" value="Choose username"/>
</form>
</div>
</body>

<?php 
if (isset($_POST['username'])) {
	$_SESSION['user'] = $_POST['username'];
    $filename = $_SESSION['user'].".log";
    if (empty($_SESSION['id'])) {
    if(!(file_exists($filename))) {
        file_put_contents($filename, json_encode(array()), LOCK_EX) or print("File writing failed.");	 
        }
     } 
     header("location:index.php");
     die();
    }

?>

</html>
