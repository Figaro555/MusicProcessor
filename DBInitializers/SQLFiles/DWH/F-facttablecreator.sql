create table Fact_table(
    channel_id INT NOT NULL,
    video_id INT NOT NULL,
    date_id int not null,
    time_id int not null,
    like_count INT NOT NULL,
    view_count INT NOT NULL,
    PRIMARY KEY (channel_id, video_id, date_id, time_id),
    CONSTRAINT fk_channel_id FOREIGN KEY (channel_id) REFERENCES D_channel(id),
    CONSTRAINT fk_video_id FOREIGN KEY (video_id) REFERENCES D_video(id),
    CONSTRAINT fk_date_id FOREIGN KEY (date_id) REFERENCES D_date(id),
    CONSTRAINT fk_time_id FOREIGN KEY (time_id) REFERENCES D_time(id)
);