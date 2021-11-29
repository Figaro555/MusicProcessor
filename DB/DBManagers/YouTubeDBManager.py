from Connectors.DB.PostgresConnector import PostgresConnector
from DB.DBManagers.AbstractDBManager import AbstractDBManager
from DB.Initializers.YouTube.YouTubeInitializer import YouTubeInitializer
from DB.Loaders.YouTube.ChannelLoader import ChannelLoader
from DB.Loaders.YouTube.VideoLoader import VideoLoader


class YouTubeDBManager(AbstractDBManager):
    def __init__(self):
        self.connector = PostgresConnector()
        self.initializer = YouTubeInitializer()
        self.video_loader = VideoLoader(self.connector)
        self.channel_loader = ChannelLoader(self.connector)

        self.initializer.create_tables(self.connector)

    def process_data(self, data):
        for channel in data:
            channel_id = self.channel_loader.load(channel)
            for video in channel.videos:
                self.video_loader.load(video, channel_id)
