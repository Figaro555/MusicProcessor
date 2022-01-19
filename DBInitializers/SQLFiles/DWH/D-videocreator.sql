create table D_video(
    id SERIAL PRIMARY KEY NOT NULL,
    youtube_id VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    description varchar NOT NULL
);