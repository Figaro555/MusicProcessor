CREATE TABLE if not exists Tracks(
    id SERIAL PRIMARY KEY NOT NULL,
    author VARCHAR(180) NOT NULL ,
    song VARCHAR(180) NOT NULL,
    duration REAL NOT NULL
);


CREATE TABLE if not exists Section(
    id SERIAL PRIMARY KEY NOT NULL,
    start REAL,
    duration REAL,
    loudness REAL,
    track_id INT NOT NULL,
    CONSTRAINT fk_track_id FOREIGN KEY (track_id) REFERENCES Tracks(id)
);



CREATE TABLE if not exists Segment(
    id SERIAL PRIMARY KEY NOT NULL,
    start REAL,
    duration REAL,
    loudness_start REAL,
    loudness_max_time REAL,
    loudness_max REAL,
    track_id INT NOT NULL,
    CONSTRAINT fk_track_id FOREIGN KEY (track_id) REFERENCES Tracks(id)
);