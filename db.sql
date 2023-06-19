CREATE TABLE logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    log_name TEXT NOT NULL,
    log_duration NUMERIC,
    log_break BOOLEAN NOT NULL,
    log_break_duration NUMERIC,
    log_date DATE,
    FOREIGN KEY(user_id) REFERENCES users(id)
);