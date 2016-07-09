<?php
var_dump($_POST);
#   uloz a presmeruj na dalsie
session_start();
  
if(empty($_SESSION['user'])) {
   if(empty($_POST['user'])) {
      header('Location:login.php');
      exit(); 
      }
    else {
	  $_SESSION['user'] = $_POST['user'];		
   }
}
if (isset($_POST)) {
   
   $idx = $_POST["idx"];
   $filename = $_SESSION['user'].".log";
   $file = file_get_contents($filename, FILE_USE_INCLUDE_PATH);
   $data = json_decode($file, true);
   $data[$idx] = $_POST;
   file_put_contents($filename, json_encode($data), LOCK_EX) or print("File writing failed.");	
   header("Location: index.php");
   die();
}

?>

