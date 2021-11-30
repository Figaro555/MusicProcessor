import DBLoader
from project.Entities.Kaggle.TestsOnData.Section import Section
from project.Entities.Kaggle.TestsOnData.Segment import Segment
from project.Entities.Kaggle.TestsOnData.Track import Track
from project.DataLake.PseudoDataLake import PseudoDataLake


def main():
    pseudo_data_lake = PseudoDataLake()
    local_pseudo_data_warehouse = []
    print("[INFO] data was downloaded")

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

        try:
            dbl = DBLoader(local_pseudo_data_warehouse)
            dbl.create_tables()
            dbl.load()
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL", _ex)
        finally:
            if dbl.connection:
                dbl.connection.close()


if __name__ == '__main__':
    main()
