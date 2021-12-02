from project.DB.Loaders.AbstractLoader import AbstractLoader


class SegmentLoader(AbstractLoader):
    def load(self, segment, track_id):
        with self.connector.get_connection().cursor() as cursor:
            segment_insert_queue = """  INSERT INTO Segment
                                        (start, duration, loudness_start, loudness_max_time, loudness_max, track_id)  
                                        VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(segment_insert_queue, (
                segment.start, segment.duration, segment.loudness_start, segment.loudness_max_time,
                segment.loudness_max, track_id))
            print("[INFO] Inserted segment", segment.start, "to track", track_id)
