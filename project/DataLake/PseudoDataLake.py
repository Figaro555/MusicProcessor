import json
import os
from collections import defaultdict


class PseudoDataLake:
    resource_path = "Resources"
    json_map = defaultdict(dict)

    def __init__(self, downloader_list):
        for downloader in downloader_list:
            downloader.save(self.resource_path)

        for root, dirs, files in os.walk(self.resource_path):
            for file in files:
                if file.endswith(".json"):
                    parsed_json = json.load(open(root + "/" + file, "r", encoding="utf-8"))
                    category_name = os.path.basename(root)
                    PseudoDataLake.json_map[category_name] = {**PseudoDataLake.json_map[category_name], **parsed_json}
