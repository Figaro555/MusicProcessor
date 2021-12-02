CREATE TABLE if not exists Section(
    id SERIAL PRIMARY KEY NOT NULL,
    start REAL,
    duration REAL,
    loudness REAL,
    track_id INT NOT NULL,
    CONSTRAINT fk_track_id FOREIGN KEY (track_id) REFERENCES Tracks(id)
);