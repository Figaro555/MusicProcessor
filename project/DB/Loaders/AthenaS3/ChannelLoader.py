import json

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class ChannelLoader(AbstractLoader):
    def load(self, channels):
        s3 = self.connector.get_connection()
        with open("tmp/channel.json", "w", encoding="utf-8") as f:
            for i, channel in enumerate(channels):
                s = json.dumps(channel)
                f.write(s)
                if i != len(channels) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('tmp/channel.json', bucket_name, 'Athena/src/Channel/channel.json')
