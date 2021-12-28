import json
from collections import defaultdict

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class PFactLoader(AbstractLoader):
    def load(self, facts):
        s3 = self.connector.get_connection()

        dd = defaultdict(list)

        for v in facts:
            dd[v["channel_id"]].append(v)

        for c_id in dd.keys():
            with open("tmp/" + c_id + "data.json", "w") as f:
                for i, fact in enumerate(dd[c_id]):
                    s = json.dumps(fact)
                    f.write(s)
                    if i != len(facts) - 1:
                        f.write(",")
                    f.write("\n")
            s3.meta.client.upload_file("tmp/" + c_id + 'data.json', bucket_name,
                                       'Athena/src/Fact/channel_id=' + c_id + '/data.json')
