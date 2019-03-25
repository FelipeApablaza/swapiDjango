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

  <table class="table">
  <tr>
  <th>Película</th>
  <th>Año</th>
  <th>Director</th>
  <th>Productores</th>
  <th>Episodio</th>
  </tr>

  {% for f in films%}
  <tr>
    <td><a href=film/{{f.id}} > {{f.title}}</td>
    <td>{{ f.date}}</td>
    <td>{{ f.director}}</td>
    <td>{{ f.producer}}</td>
    <td>{{ f.episode}}</td>
  </tr>
  {% endfor %}


</table>
</div>


</body>
</html>
