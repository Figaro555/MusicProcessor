CREATE TABLE Tracks(
    id SERIAL PRIMARY KEY NOT NULL,
    author VARCHAR(50) NOT NULL ,
    song VARCHAR(50) NOT NULL,
    duration REAL NOT NULL
);


CREATE TABLE Section(
    id SERIAL PRIMARY KEY NOT NULL,
    start REAL,
    duration REAL,
    loudness REAL
);

ALTER TABLE Section ADD track_id INT NOT NULL;
ALTER TABLE Section ADD CONSTRAINT fk_track_id FOREIGN KEY (track_id) REFERENCES Tracks(id);

CREATE TABLE Segment(
    id SERIAL PRIMARY KEY NOT NULL,
    start REAL,
    duration REAL,
    loudness_start REAL,
    loudness_max_time REAL,
    loudness_max REAL
);
ALTER TABLE Segment ADD track_id INT NOT NULL;
ALTER TABLE Segment ADD CONSTRAINT fk_track_id FOREIGN KEY (track_id) REFERENCES Tracks(id);