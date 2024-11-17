-- SQLite

--Create Tables
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
CREATE TABLE transcription (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    file_name TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

--For Troubleshooting
SELECT * FROM users;
SELECT * FROM transcription;

--For Cleaning Up
DELETE FROM transcription WHERE id > 0;
DELETE FROM users WHERE id > 0;