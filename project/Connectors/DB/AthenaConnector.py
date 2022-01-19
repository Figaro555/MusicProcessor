from time import time

import boto3

from project.Connectors.AbstractConnector import AbstractConnector


class AthenaConnector(AbstractConnector):
    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()
            try:
                self.connection = boto3.client("athena")
            except Exception as _ex:
                print("[ERROR] Error while creating connection with S3", _ex)
        return self.connection
