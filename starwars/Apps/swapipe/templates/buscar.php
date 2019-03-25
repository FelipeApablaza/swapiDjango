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

  <table style="width:100%">
            <tr>
              <th>Películas</th>
              <th class="normal">{% if flista %}
                    {%for f in flista%}
                      <a href=https://feapablaza.herokuapp.com/film/{{f.id}} > {{ f.title }}
                    {%endfor%}
                  {% endif %}
                  {% if not flista %}
                    <p>sin resultados</p>
                  {% endif %}
              </th>
            </tr>
            <tr>
              <th>Personajes</th>
              <th class="normal">{% if clista %}
                    {%for c in clista %}
                      <a href=https://feapablaza.herokuapp.com/character/{{c.id}} > {{ c.name }}
                    {%endfor%}
                  {% endif %}
                  {% if not clista %}
                    <p>sin resultados</p>
                  {% endif %}
              </th>
            </tr>

            <tr>
              <th>Naves</th>
              <th class="normal">{% if slista %}
                    {%for s in slista%}
                      <a href=https://feapablaza.herokuapp.com/film/{{s.id}}> {{ s.name }}
                    {%endfor%}
                  {% endif %}
                  {% if not slista %}
                    <p>sin resultados</p>
                  {% endif %}
              </th>
            </tr>

            <tr>
              <th>Planetas</th>

              <th class="normal">{% if plista %}
                    {%for p in plista%}
                      <a href=https://feapablaza.herokuapp.com/film/{{p.id}} > {{ p.name }}
                    {%endfor%}
                  {% endif %}
                  {% if not plista %}
                    <p>sin resultados</p>
                  {% endif %}
              </th>
            </tr>
  </table>





</body>
</html>
