import json
from collections import defaultdict

from AWSDownloader import AWSDownloader
from Configs.AWSconfig import bucket_name


class PseudoDataLake:
    resource_path = "./Resources"
    json_map = defaultdict(dict)

    def __init__(self):
        aws_d = AWSDownloader()
        file_generator = aws_d.download_s3_folder(aws_d.s3_resources, bucket_name, 'Resources', 'Resources')

        for file in file_generator:
            if file.endswith(".json"):
                parsed_json = json.load(open(file, "r", encoding="utf-8"))
                category_name = file.split("/")[-2]
                PseudoDataLake.json_map[category_name] = {**PseudoDataLake.json_map[category_name], **parsed_json}

