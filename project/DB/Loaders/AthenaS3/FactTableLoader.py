import json

from project.Configs.BucketConfig import bucket_name
from project.DB.Loaders.AbstractLoader import AbstractLoader


class FactLoader(AbstractLoader):
    def load(self, facts):
        s3 = self.connector.get_connection()
        with open("tmp/fact.json", "w") as f:
            for i, fact in enumerate(facts):
                s = json.dumps(fact)
                f.write(s)
                if i != len(facts) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('tmp/fact.json', bucket_name, 'Athena/src/Facts/fact.json')
