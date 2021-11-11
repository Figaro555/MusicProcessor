import glob
import json


class PseudoDataLake:
    resource_path = "./Resources"
    maps_list = []

    def __init__(self):
        for file in glob.glob(PseudoDataLake.resource_path + "/**/*.json"):
            parsed_json = json.load(open(file, "r", encoding="utf-8"))
            PseudoDataLake.maps_list.append(parsed_json)
