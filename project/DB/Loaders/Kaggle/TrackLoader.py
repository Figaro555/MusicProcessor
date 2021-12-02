from project.DB.Loaders.AbstractLoader import AbstractLoader


class TrackLoader(AbstractLoader):
    def load(self, track):
        with self.connector.get_connection().cursor() as cursor:
            track_insert_queue = """    INSERT INTO Tracks
                                            (author, song, duration)  
                                            VALUES (%s, %s, %s) RETURNING id"""
            cursor.execute(track_insert_queue, (track.artist, track.song_name, track.duration))

            print("[INFO] Inserted track", track.song_name)
            return cursor.fetchone()[0]
