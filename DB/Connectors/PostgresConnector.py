import psycopg2

from Configs.RDSconfig import *
from DB.Connectors.AbstractConnector import AbstractConnector
from time import time


class PostgresConnector(AbstractConnector):

    def __init__(self):
        self.last_connection_update = 0.
        self.connection = None

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()
            try:
                self.connection = psycopg2.connect(
                    host=host,
                    user=username,
                    password=password,
                    database=db_name,
                    port=port
                )
            except Exception as _ex:
                print("[ERROR] Error while creating connection with PostgreSQL", _ex)
        return self.connection
