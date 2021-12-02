from project.DB.Loaders.AbstractLoader import AbstractLoader


class ChannelLoader(AbstractLoader):
    def load(self, channel):
        with self.connector.get_connection().cursor() as cursor:
            channel_insert_queue = """    INSERT INTO Channel
                                                (youtube_id, title, video_count, view_count, hidden_subscriber_count) 
                                                VALUES (%s, %s, %s, %s, %s) RETURNING id;"""
            cursor.execute(channel_insert_queue, (
                channel.channel_id, channel.title, channel.video_count, channel.view_count,
                channel.hidden_subscriber_count))
            print("[INFO] Inserted channel", channel.title)
            return cursor.fetchone()[0]
