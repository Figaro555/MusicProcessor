import os

import boto3

from Configs.BucketConfig import *
from DataLake.Loaders.AbstractDownloader import AbstractDownloader


class S3Downloader(AbstractDownloader):

    def download_files(self, local_resource_path):
        self.local_resource_path = local_resource_path

        bucket = self.s3_resources.Bucket(bucket_name)
        for obj in bucket.objects.filter(Prefix=resource_folder):
            target = obj.key if self.local_resource_path is None \
                else os.path.join(self.local_resource_path, os.path.relpath(obj.key, resource_folder))
            if not os.path.exists(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            if obj.key[-1] != '/':
                bucket.download_file(obj.key, target)

    def __init__(self):
        self.local_resource_path = ""
        self.s3_resources = boto3.resource("s3", aws_access_key_id=access_key,
                                           aws_secret_access_key=secret_access_key)

