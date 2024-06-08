<?php
$servername = "localhost:5432";
$username = "postgres";
$password = "Dynamic01:";
$dbname = "pbl-tws";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$processor_name = isset($_GET['processor_name']) ? $_GET['processor_name'] : '';
$ram = isset($_GET['ram']) ? $_GET['ram'] : '';
$storage_capacity = isset($_GET['storage_capacity']) ? $_GET['storage_capacity'] : '';
$storage_type = isset($_GET['storage_type']) ? $_GET['storage_type'] : '';
$graphic = isset($_GET['graphic']) ? $_GET['graphic'] : '';
$price_min = isset($_GET['price_min']) ? $_GET['price_min'] : '';
$price_max = isset($_GET['price_max']) ? $_GET['price_max'] : '';

$query = "SELECT * FROM laptop WHERE 1=1";

if ($processor_name) {
    $query .= " AND processor_name=?";
}
if ($ram) {
    $query .= " AND ram=?";
}
if ($storage_capacity) {
    $query .= " AND storage_capacity=?";
}
if ($storage_type) {
    $query .= " AND storage_type=?";
}
if ($graphic) {
    $query .= " AND graphic=?";
}
if ($price_min || $price_max) {
    $query .= " AND CAST(REPLACE(SUBSTRING(price, 3), ',', '') AS UNSIGNED) BETWEEN ? AND ?";
}

$stmt = $conn->prepare($query);

$types = "";
$params = [];

if ($processor_name) {
    $types .= "s";
    $params[] = $processor_name;
}
if ($ram) {
    $types .= "s";
    $params[] = $ram;
}
if ($storage_capacity) {
    $types .= "s";
    $params[] = $storage_capacity;
}
if ($storage_type) {
    $types .= "s";
    $params[] = $storage_type;
}
if ($graphic) {
    $types .= "s";
    $params[] = $graphic;
}
if ($price_min || $price_max) {
    $types .= "ii";
    $params[] = $price_min ?: 0;
    $params[] = $price_max ?: PHP_INT_MAX;
}

$stmt->bind_param($types, ...$params);
$stmt->execute();
$result = $stmt->get_result();

echo "Query results:<br>";
while ($row = $result->fetch_assoc()) {
    foreach ($row as $column => $value) {
        echo "$column: $value | ";
    }
    echo "<br>";
}

$conn->close();
?>
