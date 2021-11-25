CREATE TABLE if not exists Channel(
    id SERIAL PRIMARY KEY NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL,
    video_count INT NOT NULL,
    view_count INT NOT NULL,
    hidden_subscriber_count bool NOT NULL
);


CREATE TABLE if not exists Video(
    id SERIAL PRIMARY KEY NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL,
    like_count INT NOT NULL,
    view_count INT NOT NULL,
    channel_id INT NOT NULL,
    CONSTRAINT fk_channel_id FOREIGN KEY (channel_id) REFERENCES Channel(id)
);