CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL);
CREATE TABLE logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    log_name TEXT NOT NULL,
    log_duration NUMERIC,
    log_break BOOLEAN NOT NULL,
    log_break_duration NUMERIC,
    log_date DATE
);
CREATE TABLE times (
log_time TEXT,
log_id INTEGER,
log_break_time INTEGER
);