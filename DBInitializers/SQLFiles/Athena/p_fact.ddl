CREATE EXTERNAL TABLE IF NOT EXISTS
mdatabase.p_fact (
    video_id string,
    date_id int,
    time_id int,
    view_count int,
    like_count int

)PARTITIONED BY (channel_id string)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
 LOCATION 's3://myprojectbucket111/Athena/src/Fact/';