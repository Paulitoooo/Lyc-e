<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title></title>
  </head>
  <body>
	Ouverture de la page</br>
	récupération des données...
    <?php
	$nom = htmlspecialchars($POST['leNom']);
	echo $leNom
	?>
	Ecriture du fichier texte...
	<?php
	$file = fopen("../depots/Paul_Gresset/PaulG.txt","w+");
	fwrite($file;$nom);
	fclose($file);
	?>
    
  </body>
</html>
