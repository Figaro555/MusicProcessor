import psycopg2

from Enteties.Section import Section
from Enteties.Segment import Segment
from Enteties.Track import Track
from PseudoDataLake import PseudoDataLake
from Configs.config import host, user, password, db_name, port


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

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port

        )

        for track in local_pseudo_data_warehouse:
            with connection.cursor() as cursor:
                track_insert_queue = """INSERT INTO Tracks(author, song, duration)  VALUES (%s, %s, %s) RETURNING id"""
                cursor.execute(track_insert_queue, (track.artist, track.song_name, track.duration))
                track_id = cursor.fetchone()[0]

                for segment in track.segments:
                    segment_insert_queue = """INSERT INTO Segment(start, duration, loudness_start, loudness_max_time, loudness_max, track_id)  VALUES (%s, %s, %s, %s, %s, %s)"""
                    cursor.execute(segment_insert_queue, (
                        segment.start, segment.duration, segment.loudness_start, segment.loudness_max_time,
                        segment.loudness_max, track_id))

                for section in track.sections:
                    section_insert_queue = """INSERT INTO Section(start, duration, loudness, track_id)  VALUES (%s, %s, %s, %s)"""
                    cursor.execute(section_insert_queue, (
                        section.start, section.duration, section.loudness, track_id))

                print(track_id)
            print(track.song_name)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    main()
