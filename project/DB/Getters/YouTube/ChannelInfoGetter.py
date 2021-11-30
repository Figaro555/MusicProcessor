class ChannelInfoGetter:
    def __init__(self, connector):
        self.connector = connector


    def get_videos_count(self):
        with self.connector.get_connection().cursor() as cursor:
            channel_getting_queue = """    SELECT title, video_count from Channel;"""
            cursor.execute(channel_getting_queue)
            return cursor.fetchall()
