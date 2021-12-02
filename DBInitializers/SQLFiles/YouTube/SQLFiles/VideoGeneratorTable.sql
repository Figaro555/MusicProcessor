CREATE TABLE if not exists Video(
    id SERIAL PRIMARY KEY NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    like_count INT NOT NULL,
    view_count INT NOT NULL,
    channel_id INT NOT NULL,
    CONSTRAINT fk_channel_id FOREIGN KEY (channel_id) REFERENCES Channel(id)
);