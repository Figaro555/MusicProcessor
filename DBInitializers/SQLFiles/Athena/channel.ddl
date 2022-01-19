CREATE EXTERNAL TABLE IF NOT EXISTS
mdatabase.channel (
    id string,
    title string,
    video_count int,
    view_count int,
    description string

)

ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
 LOCATION 's3://myprojectbucket111/Athena/src/Channel/';