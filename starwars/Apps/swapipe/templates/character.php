<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
* {box-sizing: border-box;}
body {  margin: 0;  font-family: Arial, Helvetica, sans-serif;}
.topnav {  overflow: hidden;  background-color: #e9e9e9;}
.topnav a {  float: left;  display: block;  color: black;  text-align: center;
  padding: 14px 16px;  text-decoration: none;  font-size: 17px;}
.topnav a:hover {  background-color: #ddd;  color: black;}
.topnav a.active {  background-color: red;  color: white;}
.topnav .search-container {  float: right;}
.topnav input[type=text] {  padding: 6px;  margin-top: 8px;  font-size: 17px;  border: none;}
.topnav .search-container button {  float: right;  padding: 6px 10px;  margin-top: 8px;  margin-right: 16px;
  background: #ddd;  font-size: 17px;  border: none;  cursor: pointer;}
.topnav .search-container button:hover {  background: #ccc;}
@media screen and (max-width: 600px) {
    .topnav .search-container {
    float: none;  }
  .topnav a, .topnav input[type=text], .topnav .search-container button {
    float: none;    display: block;    text-align: left;    width: 100%;
    margin: 0;    padding: 14px;  }
  .topnav input[type=text] {    border: 1px solid #ccc;  }}
</style>
</head>
<body>
<div class="topnav">
  <a class="active" href="https://feapablaza.herokuapp.com/">Home</a>
  <div class="search-container">
    <form action="https://feapablaza.herokuapp.com/buscar/">
      <input type="text" placeholder="buscar.." name="search">
      <button type="submit"><i class="fa fa-search"></i></button>
    </form>
  </div>
</div>
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
  <h1 class="text-center" >STAR WARS SWAPIPE</h1>
</div>
<div class="container">
<body>
  <table class="table">
    {% for f in character%}
    <tr><th><h1>{{f.name}}</h1></th><th></th></tr>
    <tr><th>Altura</th><th>{{f.height}}</th></tr>
    <tr><th>Peso</th><th>{{f.mass}}</th></tr>
    <tr><th>Color de pelo</th><th>{{f.hair_color}}</th></tr>
    <tr><th>Color de piel</th><th>{{f.skin_color}}</th></tr>
    <tr><th>Color de ojos</th><th>{{f.eye_color}}</th></tr>
    <tr><th>Año de nacimiento</th><th>{{f.birth_year}}</th></tr>
    <tr><th>Género</th><th>{{f.gender}}</th></tr>
    <tr><th>Planeta natal</th><th>
      {% for n in f.homeworld%}
      <a href=https://feapablaza.herokuapp.com/planet/{{n.id}} >{{n.name}}
      {%endfor%}
    </th></tr>
    <tr><th>Películas</th><th>
      {% for n in f.films%}
      <a href=https://feapablaza.herokuapp.com/film/{{n.id}} > {{n.title}}
      {%endfor%}
    </th></tr>
    <tr><th>Naves</th><th>
      {% for n in f.starships%}
      <a href=https://feapablaza.herokuapp.com/starship/{{n.id}} > {{n.name}}
      {%endfor%}
    </th></tr>
      {% endfor %}


  </table>

</div>
</body>
</html>
