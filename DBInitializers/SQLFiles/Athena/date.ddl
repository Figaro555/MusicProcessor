CREATE EXTERNAL TABLE IF NOT EXISTS
mdatabase.date (
    id int,
    day int,
    month int,
    year int

)ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 WITH SERDEPROPERTIES ('ignore.malformed.json' = 'true')
 LOCATION 's3://myprojectbucket111/Athena/src/Date/';