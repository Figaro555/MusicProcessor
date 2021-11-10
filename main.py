import json

from Enteties.MetaInformation import MetaInformation
from Enteties.Section import Section
from Enteties.Segment import Segment
from Enteties.Track import Track


def main():
    resource = open("Resources/KaggleTestsOnData/classical.json", "r", encoding="utf-8")
    pseudo_data_lake = json.load(resource)
    pseudo_data_warehouse = [Track(key,
                                   pseudo_data_lake[key]["artist"],
                                   pseudo_data_lake[key]["song"],
                                   MetaInformation(pseudo_data_lake[key]["meta"]["track"]["duration"],
                                                   [Section(section["start"],
                                                            section["duration"],
                                                            section["loudness"])
                                                    for section in pseudo_data_lake[key]["meta"]["sections"]],
                                                   [Segment(segment["start"],
                                                            segment["duration"],
                                                            segment["loudness_start"],
                                                            segment["loudness_max_time"],
                                                            segment["loudness_max"]
                                                            )
                                                    for segment in pseudo_data_lake[key]["meta"]["segments"]]
                                                   )
                                   )
                             for key in pseudo_data_lake.keys()]


if __name__ == '__main__':
    main()
