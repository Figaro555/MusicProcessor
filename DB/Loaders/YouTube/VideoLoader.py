from DB.Loaders.AbstractLoader import AbstractLoader


class VideoLoader(AbstractLoader):
    def load(self, video, channel_id):
        with self.connector.get_connection().cursor() as cursor:
            video_insert_queue = """  INSERT INTO Video
                                            (youtube_id, title, like_count, view_count, channel_id) 
                                            VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(video_insert_queue, (
                video.video_id, video.title, video.like_count, video.view_count, channel_id
            ))
            print("[INFO] Inserted video", video.title, "to channel", channel_id)
