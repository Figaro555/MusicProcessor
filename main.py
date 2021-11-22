from DB.DBLoader import DBLoader
from DB.DBLoaderRDS import DBLoaderRDS
from Enteties.Section import Section
from Enteties.Segment import Segment
from Enteties.Track import Track
from PseudoDataLake import PseudoDataLake


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
            db_loader = DBLoader(local_pseudo_data_warehouse)
            db_loader.load_data()
            db_loader.create_tables()
            db_loader.create_tracking_tables()
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL locally", _ex)
        finally:
            if db_loader.connection:
                db_loader.connection.close()

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
