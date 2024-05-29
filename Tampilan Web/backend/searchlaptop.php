<?php
header('Content-Type: application/json');

// Connect to PostgreSQL database
$conn = pg_connect("host=localhost port=5432 dbname=pbl-tws user=postgres password=Dynamic01:");

if (!$conn) {
    die("Connection failed: ". pg_last_error());
}

// Get search value from POST request
$searchValue = $_POST['searchValue'];
$names = $_POST['name'];
$ram = $_POST['ram'];
$storage_capacity = $_POST['storage_capacity'];
$processor_brand = $_POST['processor_brand'];
$graphic = $_POST['graphic'];
$price= $_POST['price'];

// Create query to search for laptops
$query = "SELECT * FROM laptop WHERE name ILIKE $1";

$params = array();
$params[] = "%$searchValue%";

if ($names != 'all') {
    $query .= " AND names = $2";
    $params[] = $name;
}

if ($ram != 'all') {
    $query .= " AND ram = $3";
    $params[] = $ram;
}

if ($rom != 'all') {
    $query .= " AND rom = $4";
    $params[] = $rom;
}

if ($processor_brand != 'all') {
    $query .= " AND processor_brand = $5";
    $params[] = $processor_brand;
}

if ($graphic != 'all') {
    $query .= " AND graphic = $6";
    $params[] = $graphic;
}

if ($price != 'all') {
    $query .= " AND price = $7";
    $params[] = $price;
}

// Execute query
$result = pg_query_params($conn, $query, $params);

// Fetch results
$laptops = array();
while ($row = pg_fetch_assoc($result)) {
    $laptops[] = array(
        'id' => $row['id'],
        'name' => $row['name'],
        'brand' => $row['brand'],
        'cpu' => $row['cpu'],
        'ram' => $row['ram'],
        'rom' => $row['rom'],
        'storage_type' => $row['storage_type'],
        'screen_size' => $row['screen_size'],
        'gpu' => $row['gpu'],
        'price' => $row['price']
    );
}

// Close connection
pg_free_result($result);
pg_close($conn);

// Output JSON
echo json_encode($laptops);
?>