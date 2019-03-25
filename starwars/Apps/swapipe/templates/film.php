<!DOCTYPE html>
<html>
<head>
  <title>
  </title>
</head>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
<body>
  <div class="container">
  <h1 class="text-center" >STAR WARS MOVIES</h1>
</div>
<div class="container">
<body>
  <table class="table">
    {% for f in film%}
    <tr><th>Título</th><th>{{f.title}}</th></tr>
    <tr><th>Episodio</th><th>{{f.episode}}</th></tr>
    <tr><th>Comentario</th><th>{{f.opening}}</th></tr>
    <tr><th>Director</th><th>{{f.director}}</th></tr>
    <tr><th>Productor</th><th>{{f.producer}}</th></tr>
    <tr><th>Año</th><th>{{f.date}}</th></tr>
    <tr><th>Naves</th><th>
      {% for n in f.starships%}
      <a href=http://localhost:3000/starship/{{n.id}} > {{n.name}}
      {%endfor%}
    </th></tr>
    <tr><th>Planetas</th><th>
      {% for n in f.planets%}
      <a href=planet/{{n.id}} > {{n.name}}
      {%endfor%}
    </th></tr>
    <tr><th>Personajes</th><th>
      {% for n in f.characters%}
      <a href=character/{{n.id}} > {{n.name}}
      {%endfor%}
    </th></tr>
    {% endfor %}


  </table>
</body>
</html>
