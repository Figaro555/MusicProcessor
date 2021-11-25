import json
import os
from collections import defaultdict


class PseudoDataLake:
    resource_path = "Resources"
    json_map = defaultdict(dict)

    def __init__(self, downloader_list):
        for downloader in downloader_list:
            downloader.download_files(self.resource_path)

        for file in os.listdir(self.resource_path):
            if file.endswith(".json"):
                parsed_json = json.load(open(file, "r", encoding="utf-8"))
                category_name = file.split("\\")[-2]
                PseudoDataLake.json_map[category_name] = {**PseudoDataLake.json_map[category_name], **parsed_json}
