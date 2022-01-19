import json

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class VideoLoader(AbstractLoader):
    def load(self, videos):
        s3 = self.connector.get_connection()
        with open("tmp/video.json", "w", encoding="utf-8") as f:
            for i, video in enumerate(videos):
                s = json.dumps(video, ensure_ascii=False)
                f.write(s)
                if i != len(videos) - 1:
                    f.write(",")
                f.write("\n")
            s3.meta.client.upload_file('tmp/video.json', bucket_name, 'Athena/src/Video/video.json')
