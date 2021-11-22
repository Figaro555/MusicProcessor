import psycopg2

from Configs.config import host, user, password, db_name, port


class DBLoader:

    def __init__(self, local_dwh):
        self.local_DWH = local_dwh

    def create_tracking_tables(self):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port

            )
            with connection.cursor() as cursor:
                cursor.execute(open("DB/generate_tracking_tables.sql", "r").read())
        except Exception as _ex:
            print("[ERROR] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()

    def load_data(self):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                port=port

            )

            for track in self.local_DWH:
                with connection.cursor() as cursor:
                    track_insert_queue = """    INSERT INTO
                                                Tracks(author, song, duration)  
                                                VALUES (%s, %s, %s) RETURNING id"""
                    cursor.execute(track_insert_queue, (track.artist, track.song_name, track.duration))
                    track_id = cursor.fetchone()[0]

                    for segment in track.segments:
                        segment_insert_queue = """  INSERT INTO 
                                                    Segment(start, duration, loudness_start, loudness_max_time, loudness_max, track_id)  
                                                    VALUES (%s, %s, %s, %s, %s, %s)"""
                        cursor.execute(segment_insert_queue, (
                            segment.start, segment.duration, segment.loudness_start, segment.loudness_max_time,
                            segment.loudness_max, track_id))

                    for section in track.sections:
                        section_insert_queue = """  INSERT INTO 
                                                    Section(start, duration, loudness, track_id)
                                                    VALUES (%s, %s, %s, %s)"""
                        cursor.execute(section_insert_queue, (
                            section.start, section.duration, section.loudness, track_id))

        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
        finally:
            if connection:
                connection.close()
