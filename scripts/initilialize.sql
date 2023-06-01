-- Set mysql native password rule
ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY 'admin123';
-- Create database
CREATE DATABASE auth_backend;