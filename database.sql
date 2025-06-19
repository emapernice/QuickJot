CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE users (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100),
    last_names  VARCHAR(255),
    email       VARCHAR(255) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    date        DATE NOT NULL
) ENGINE=InnoDB;

CREATE TABLE notes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL,
    title       VARCHAR(255) NOT NULL,
    description MEDIUMTEXT,
    date        DATE NOT NULL,
    CONSTRAINT fk_note_user FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=InnoDB;
