import os

from Configs.BucketConfig import *
from Connectors.DL.S3Connector import S3Connector
from DataLake.DataSavers.AbstractDataSaver import AbstractDataSaver


class S3DataSaver(AbstractDataSaver):
    def __init__(self):
        self.connector = S3Connector()

    def save(self, resource_path):
        bucket = self.connector.get_connection().Bucket(bucket_name)
        for obj in bucket.objects.filter(Prefix=resource_folder):
            target = obj.key if resource_path is None \
                else os.path.join(resource_path, os.path.relpath(obj.key, resource_folder))
            if not os.path.exists(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            if obj.key[-1] != '/':
                bucket.download_file(obj.key, target)
