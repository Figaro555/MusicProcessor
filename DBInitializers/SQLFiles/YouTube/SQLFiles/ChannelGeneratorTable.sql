CREATE TABLE if not exists Channel(
    id SERIAL PRIMARY KEY NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    video_count INT NOT NULL,
    view_count INT NOT NULL,
    hidden_subscriber_count bool NOT NULL
);