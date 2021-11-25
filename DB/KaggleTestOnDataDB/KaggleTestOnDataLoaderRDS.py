from DB.AbstractDBLoader import AbstractDBLoader


class KaggleTestOnDataLoaderRDS(AbstractDBLoader):
    def __init__(self, local_dwh):
        self.local_DWH = local_dwh
        self.connection = None
        self.create_connection()
        self.create_tables("DB/KaggleTestOnDataDB/generate_tables.sql")

    def insert_track(self, cursor, track):
        track_insert_queue = """    INSERT INTO
                                                        Tracks(author, song, duration)  
                                                        VALUES (%s, %s, %s) RETURNING id"""
        cursor.execute(track_insert_queue, (track.artist, track.song_name, track.duration))

        print("[INFO] Inserted track", track.song_name)
        return cursor.fetchone()[0]

    def insert_segment(self, cursor, segment, track_id, track_song_name):
        segment_insert_queue = """  INSERT INTO 
                                                            Segment(start, duration, loudness_start, loudness_max_time, loudness_max, track_id)  
                                                            VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(segment_insert_queue, (
            segment.start, segment.duration, segment.loudness_start, segment.loudness_max_time,
            segment.loudness_max, track_id))
        print("[INFO] Inserted segment", segment.start, "to track", track_song_name)

    def insert_section(self, cursor, section, track_id, track_song_name):
        section_insert_queue = """  INSERT INTO 
                                                            Section(start, duration, loudness, track_id)
                                                            VALUES (%s, %s, %s, %s)"""
        cursor.execute(section_insert_queue, (
            section.start, section.duration, section.loudness, track_id))

        print("[INFO] Inserted section", section.start, "to track", track_song_name)

    def load(self):
        for track in self.local_DWH:
            with self.connection.cursor() as cursor:
                try:
                    track_id = self.insert_track(cursor, track)

                    for segment in track.segments:
                        self.insert_segment(cursor, segment, track_id, track.song_name)
                    for section in track.sections:
                        self.insert_section(cursor, section, track_id, track.song_name)
                except Exception as _ex:
                    print("[ERROR] Error while inserting data with PostgreSQL", _ex)
                finally:
                    if self.connection:
                        self.connection.close()
                        self.create_connection()
