import os

import boto3

from Configs.AWSconfig import access_key, secret_access_key


class AWSDownloader:

    def __init__(self):
        self.s3_resources = boto3.resource("s3", aws_access_key_id=access_key,
                                           aws_secret_access_key=secret_access_key)

    def download_s3_folder(self, s3, bucket, s3_folder, local_dir):
        bucket = s3.Bucket(bucket)
        for obj in bucket.objects.filter(Prefix=s3_folder):
            target = obj.key if local_dir is None \
                else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
            if not os.path.exists(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            if obj.key[-1] != '/':
                bucket.download_file(obj.key, target)
                yield target
                os.remove(target)
