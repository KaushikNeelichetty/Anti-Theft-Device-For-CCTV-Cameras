<?php
	$cam=isset($_GET['camera'])?$_GET['camera']:"";
	
	if($cam==1) {
		$content1=file_get_contents('camera1.txt',FILE_TEXT);
		echo $content1 . "\xA" ;
	}
	else if($cam==2) {
		$content2=file_get_contents('camera2.txt',FILE_TEXT);
		echo $content2 . "\xA" ;
	}	
?>