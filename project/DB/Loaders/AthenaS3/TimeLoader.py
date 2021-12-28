import json

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class TimeLoader(AbstractLoader):
    def load(self, data):
        s3 = self.connector.get_connection()
        with open("tmp/time.json", "w") as f:
            for i, time in enumerate(data):
                s = json.dumps(time)
                f.write(s)
                if i != len(data) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('tmp/time.json', bucket_name, 'Athena/src/Time/time.json')
