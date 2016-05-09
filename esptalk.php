<?php
		$safe=isset($_GET['safe'])?$_GET['safe']:"";
		$cam=isset($_GET['camera'])?$_GET['camera']:"";
		
		if($cam==1 and $safe==0) {
			file_put_contents('camera1.txt',"unsafe\n");
		}
		else if($cam==2 and $safe==0) {
			file_put_contents('camera2.txt',"unsafe\n");
		}
		else if($safe==1 and $cam==1) {
			file_put_contents('camera1.txt',"safe\n");
		}
		else if($safe==1 and $cam==2) {
			file_put_contents('camera2.txt',"safe\n");
		}
?>