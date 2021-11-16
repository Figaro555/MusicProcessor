import glob
import json
from collections import defaultdict

from AWSDownloader import AWSDownloader


class PseudoDataLake:
    resource_path = "./Resources"
    json_map = defaultdict(dict)

    def __init__(self):
        aws_d = AWSDownloader()

        for file in glob.glob(PseudoDataLake.resource_path + "/**/*.json"):
            parsed_json = json.load(open(file, "r", encoding="utf-8"))
            category_name = file.split("\\")[-2]
            PseudoDataLake.json_map[category_name] = {**PseudoDataLake.json_map[category_name], **parsed_json}
