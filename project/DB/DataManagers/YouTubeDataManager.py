from project.Connectors.DB.PostgresConnector import PostgresConnector
from project.DB.DataManagers.AbstractDataManager import AbstractDataManager
from project.DB.Loaders.YouTube.ChannelLoader import ChannelLoader
from project.DB.Loaders.YouTube.VideoLoader import VideoLoader


class YouTubeDataManager(AbstractDataManager):
    def __init__(self):
        self.connector = PostgresConnector()

        self.video_loader = VideoLoader(self.connector)
        self.channel_loader = ChannelLoader(self.connector)

    def process_data(self, data):
        for channel in data:
            channel_id = self.channel_loader.load(channel)
            for video in channel.videos:
                self.video_loader.load(video, channel_id)
