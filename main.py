from DB.KaggleTestOnDataDB.DBLoaderRDS import DBLoaderRDS
from Enteties.KaggleTestOnData.Section import Section
from Enteties.KaggleTestOnData.Segment import Segment
from Enteties.KaggleTestOnData.Track import Track
from DataLake.PseudoDataLake import PseudoDataLake


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
            dbl = DBLoaderRDS(local_pseudo_data_warehouse)
            dbl.create_tables()
            dbl.load()
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL", _ex)
        finally:
            if dbl.connection:
                dbl.connection.close()


if __name__ == '__main__':
    main()
