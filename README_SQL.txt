CREATE DATABASE IF NOT EXISTS techshop_db;
USE techshop_db;

CREATE TABLE IF NOT EXISTS produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prix DECIMAL(10,2),
    stock INT
);

CREATE TABLE IF NOT EXISTS ventes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produit_id INT,
    quantite INT,
    total DECIMAL(10,2),
    date_vente TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produit_id) REFERENCES produits(id)
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin', 'employe') DEFAULT 'employe'
);

INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin');
