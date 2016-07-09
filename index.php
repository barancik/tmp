
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<link type="text/css" rel="stylesheet" href="new.css" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	  
	 <?php
	  session_destroy();
	  session_start();
	   if(empty($_SESSION['user']) || $_SESSION['user'] == "") {
        header('Location:login.php');
        exit(); 
      } 
	  $user = $_SESSION['user'];
	  //Need to open the file with verb and noun data
	  $data_file = "file.json";
	  if(file_exists($data_file)) {
		 $file = file_get_contents($data_file, FILE_USE_INCLUDE_PATH);
		 $annotations = json_decode($file, true);                
	  } else {
		 print("Error");	 
	  };
	  
	  //Pick a new index
	  $filename = $_SESSION['user'].".log";
      $file = file_get_contents($filename, FILE_USE_INCLUDE_PATH);
      $data = json_decode($file, true);
      if (sizeof($data) > 180) {
		  print ("Thank you for your help!");
		  exit();
	   }
	  $idx = rand (0 , 200 ); 
	  while (isset($data[$idx])) {$idx = rand (0 , 200 );}
      $data = $annotations[$idx];
	?>
	  
</head>

<body>
	<div class="container">
	<form action="save.php" method="post">
	
  <?php 
	if (isset($data)) {
		print "<input type=\"hidden\" name=\"idx\" value=\"{$idx}\"/>";
		print "<input type=\"hidden\" name=\"user\" value=\"{$user}\"/>";
		$source_file = 	$translation['file'];
		print "<input type=\"hidden\" name=\"source\" value=\"{$source_file}\"/>";
		print '<table>';
		print '<br><br>Please rate quality of the following sentences from <b>best</b> (1) to <b>worst</b>(4). Ties are allowed.<br><br>';
		print  '<b>Source sentence: </b>';
			print_r($data['source']['text']);
		foreach ($data['translations'] as $translation) {
			print '<tr valign="bottom">';
			$source = $translation['file'];
			print  "<td style=\"text-align: center\"><label for=\"{$source}_1\">1<br><input type=\"radio\" name=\"{$source}\" value=\"1\"></label></td>";
			print  "<td style=\"text-align: center\"><label for=\"{$source}_2\">2<br><input type=\"radio\" name=\"{$source}\" value=\"2\"></label></td>";
			print  "<td style=\"text-align: center\"><label for=\"{$source}_3\">3<br><input type=\"radio\" name=\"{$source}\" value=\"3\"></label></td>";
			print  "<td style=\"text-align: center\"><label for=\"{$source}_4\">4<br><input type=\"radio\" name=\"{$source}\" value=\"4\"></label></td>";
			print  "<td valign=\"middle\">&nbsp;&nbsp;";
			print_r($translation['text']); 
			print "</td></tr> <br>";
			
		}
			print '</table>';
			print '<p style="text-align: center;"><input type="submit" value="Send"/></p>';
			
			
			
		
		
		} 
		
	?>
		
		</form>
	</div>
</body>
</html>
