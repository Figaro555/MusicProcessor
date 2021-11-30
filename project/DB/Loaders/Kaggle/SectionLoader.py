from project.DB.Loaders.AbstractLoader import AbstractLoader


class SectionLoader(AbstractLoader):
    def load(self, section, track_id):
        with self.connector.get_connection().cursor() as cursor:
            section_insert_queue = """  INSERT INTO Section
                                            (start, duration, loudness, track_id)
                                            VALUES (%s, %s, %s, %s)"""
            cursor.execute(section_insert_queue, (
                section.start, section.duration, section.loudness, track_id))
            print("[INFO] Inserted section", section.start, "to track", track_id)
