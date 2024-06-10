<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>formulaire</title>
  </head>
  <body>
    <p>Bonjour
      <?php echo htmlspecialchars($_POST['leNom']); ?>, </p>
    <script>
      //Récupérer la variable en javascrit
      var LeNom="<?php echo $_POST['leNom'] ?>";      
      alert(LeNom)
    </script>
    <?php
		if ($_POST['leNom']=='Raoul'){?>
    <div>C'est un joli nom Raoul.</div>
    <?}else{?>
    <div>C'est un joli nom mais Raoul c'est mieux.</div>
    <?}?>
  </body>
</html>
