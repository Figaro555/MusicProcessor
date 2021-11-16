from DBLoader import DBLoader
from Enteties.Section import Section
from Enteties.Segment import Segment
from Enteties.Track import Track
from PseudoDataLake import PseudoDataLake


def main():
    pseudo_data_lake = PseudoDataLake()
    local_pseudo_data_warehouse = []

    for category in pseudo_data_lake.json_map:
        local_pseudo_data_warehouse += ([Track(key,
                                               pseudo_data_lake.json_map[category][key]["artist"],
                                               pseudo_data_lake.json_map[category][key]["song"],
                                               pseudo_data_lake.json_map[category][key]["meta"]["track"][
                                                   "duration"],
                                               [Section(section["start"],
                                                        section["duration"],
                                                        section["loudness"])
                                                for section in
                                                pseudo_data_lake.json_map[category][key]["meta"]["sections"]],
                                               [Segment(segment["start"],
                                                        segment["duration"],
                                                        segment["loudness_start"],
                                                        segment["loudness_max_time"],
                                                        segment["loudness_max"]
                                                        )
                                                for segment in
                                                pseudo_data_lake.json_map[category][key]["meta"]["segments"]]

                                               )
                                         for key in pseudo_data_lake.json_map[category].keys()])
        db_loader = DBLoader(local_pseudo_data_warehouse)
        db_loader.load_data()


if __name__ == '__main__':
    main()
