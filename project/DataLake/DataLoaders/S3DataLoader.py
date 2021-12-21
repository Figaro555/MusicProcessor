import os

from project.Configs.BucketConfig import *
from project.Connectors.DL.S3Connector import S3Connector
from project.DataLake.DataLoaders.AbstractDataLoader import AbstractDataLoader


class S3DataLoader(AbstractDataLoader):
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
                print("[INFO]File was downloaded" + obj.key)
