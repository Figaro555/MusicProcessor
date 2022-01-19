import json

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class DateLoader(AbstractLoader):
    def load(self, dates):
        s3 = self.connector.get_connection()
        with open("tmp/date.json", "w") as f:
            for i, date in enumerate(dates):
                s = json.dumps(date)
                f.write(s)
                if i != len(dates) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('tmp/date.json', bucket_name, 'Athena/src/Date/date.json')
