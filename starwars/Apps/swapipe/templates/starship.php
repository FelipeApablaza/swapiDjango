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
  <!-- <a class="active" href="https://feapablaza.herokuapp.com/">Home</a> -->
  <a class="active" href="http://localhost:3000/">Home</a>
  <div class="search-container">
    <!-- <form action="https://feapablaza.herokuapp.com/buscar/">
      <form action="http://localhost:3000/buscar/">
      <input type="text" placeholder="buscar.." name="search">
      <button type="submit"><i class="fa fa-search"></i></button>
    </form> -->
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
    {% for f in starship%}
    <tr><th><h1>{{f.name}}<h1></th><th></th></tr>
    <tr><th>Modelo</th><th>{{f.model}}</th></tr>
    <tr><th>Fabricante</th><th>{{f.manufacturer}}</th></tr>
    <tr><th>Costo en creditos</th><th>{{f.cost_in_credits}}</th></tr>
    <tr><th>Largo</th><th>{{f.length}}</th></tr>
    <tr><th>Velocidad Maxima</th><th>{{f.max_atmosphering_speed}}</th></tr>
    <tr><th>Personal</th><th>{{f.crew}}</th></tr>
    <tr><th>Pasajeros</th><th>{{f.passengers}}</th></tr>
    <tr><th>Capacidad cargo</th><th>{{f.cargo_capacity}}</th></tr>
    <tr><th>Consumibles</th><th>{{f.consumables}}</th></tr>
    <tr><th>Hyperdriva Rating</th><th>{{f.hyperdrive_rating}}</th></tr>
    <tr><th>MGLT</th><th>{{f.MGLT}}</th></tr>
    <tr><th>Clase de nave</th><th>{{f.starship_class}}</th></tr>
    <tr><th>Pilotos</th><th>
      {% for n in f.pilots%}
      <!-- <a href=https://feapablaza.herokuapp.com/character/{{n.id}} > {{n.name}} -->
      <a href=http://localhost:3000/character/{{n.id}} > {{n.name}} |
      {%endfor%}
    </th></tr>
    <tr><th>Películas</th><th>
      {% for n in f.films%}
      <!-- <a href=https://feapablaza.herokuapp.com/film/{{n.id}} > {{n.title}} -->
      <a href=http://localhost:3000/film/{{n.id}} > {{n.title}} |
      {%endfor%}
    </th></tr>
    {% endfor %}


  </table>

</body>
</html>
