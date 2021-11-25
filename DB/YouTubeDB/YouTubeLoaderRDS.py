from DB.AbstractDBLoader import AbstractDBLoader


class YouTubeLoaderRDS(AbstractDBLoader):
    def __init__(self, local_dwh):
        self.local_DWH = local_dwh
        self.connection = None
        self.create_connection()
        self.create_tables("DB/YouTubeDB/generate_tables.sql")

    def insert_channel(self, cursor, channel):
        channel_insert_queue = """    INSERT INTO Channel
                                                        (youtube_id, title, video_count, view_count, hidden_subscriber_count) 
                                                        VALUES (%s, %s, %s, %s, %s) RETURNING id;"""
        cursor.execute(channel_insert_queue, (
            channel.channel_id, channel.title, channel.video_count, channel.view_count,
            channel.hidden_subscriber_count))
        print("[INFO] Inserted channel", channel.title)
        return cursor.fetchone()[0]

    def insert_video(self, cursor, video, channel_id, channel_title):
        video_insert_queue = """  INSERT INTO Video
                                                        (youtube_id, title, like_count, view_count, channel_id) 
                                                        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(video_insert_queue, (
            video.video_id, video.title, video.like_count, video.view_count, channel_id
        ))
        print("[INFO] Inserted video", video.title, "to channel", channel_title)

    def load(self):
        for channel in self.local_DWH:
            with self.connection.cursor() as cursor:
                try:
                    channel_id = self.insert_channel(cursor, channel)
                    for video in channel.videos:
                        self.insert_video(cursor, video, channel_id, channel.title)
                except Exception as _ex:
                    print("[ERROR] Error while inserting youTube data with PostgreSQL", _ex)
                finally:
                    if self.connection:
                        self.connection.close()
                        self.create_connection()
