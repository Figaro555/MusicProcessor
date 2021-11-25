from abc import ABC, abstractmethod
from Configs.RDSconfig import *
import psycopg2


class AbstractDBLoader(ABC):
    connection = None

    def create_connection(self):
        self.connection = psycopg2.connect(
            host=endpoint,
            user=master_username,
            password=master_password,
            database=initial_db_name,
            port=RDS_port
        )

    def create_tables(self, file_path):
        try:
            self.connection.set_session(autocommit=True)
            with self.connection.cursor() as cursor:
                cursor.execute(open(file_path, "r").read())
        except Exception as _ex:
            print("[ERROR] Error while creating table with PostgreSQL", _ex)

    @abstractmethod
    def load(self):
        pass
