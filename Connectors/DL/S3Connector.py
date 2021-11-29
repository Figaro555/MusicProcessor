from time import time

import boto3

from Configs.BucketConfig import *
from Connectors.AbstractConnector import AbstractConnector


class S3Connector(AbstractConnector):
    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()
            try:
                self.connection = boto3.resource("s3", aws_access_key_id=access_key,
                                                 aws_secret_access_key=secret_access_key)
            except Exception as _ex:
                print("[ERROR] Error while creating connection with S3", _ex)
        return self.connection
