<?php
$mysqli = new mysqli("mysql_prod", "root", "root", "produccion");
$result = $mysqli->query("SELECT * FROM produccion");

echo "<h1>Datos desde PROD</h1>";
echo "<ul>";
while ($row = $result->fetch_assoc()) {
    echo "<li>{$row['fabrica']}: {$row['produccion']}</li>";
}
echo "</ul>";
?>
