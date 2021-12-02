CREATE TABLE if not exists Tracks(
    id SERIAL PRIMARY KEY NOT NULL,
    author VARCHAR(180) NOT NULL ,
    song VARCHAR(180) NOT NULL,
    duration REAL NOT NULL
);