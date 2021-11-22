BEGIN;
    CREATE TABLE Processing_status(
        id SERIAL PRIMARY KEY NOT NULL,
        status VARCHAR(20) NOT NULL
    );

    INSERT INTO Processing_status(status) VALUES ('Yes'), ('No'), ('In process');
COMMIT;

CREATE TABLE if not exists Processed_files(
    id SERIAL PRIMARY KEY NOT NULL,
    file VARCHAR(120) NOT NULL
);

ALTER TABLE Processed_files ADD status_id INT NOT NULL;
ALTER TABLE Processed_files ADD CONSTRAINT fk_status_id FOREIGN KEY (status_id) REFERENCES Processing_status(id);