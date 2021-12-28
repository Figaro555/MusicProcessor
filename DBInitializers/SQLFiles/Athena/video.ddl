CREATE EXTERNAL TABLE IF NOT EXISTS
mdatabase.video (
    id string,
    title string
)ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
 LOCATION 's3://myprojectbucket111/Athena/src/Video/';
