CREATE DATABASE IF NOT EXISTS farming_db;
USE farming_db;

CREATE TABLE IF NOT EXISTS sensor_logs (
	id INT AUTO_INCREMENT PRIMARY KEY,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
	node_name VARCHAR(50),
	temperature float,
	humidity float 
);

