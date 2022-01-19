CREATE EXTERNAL TABLE IF NOT EXISTS
mdatabase.time (
    id int,
    hour int,
    minute int,
    second int

)ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
 LOCATION 's3://myprojectbucket111/Athena/src/Time/';