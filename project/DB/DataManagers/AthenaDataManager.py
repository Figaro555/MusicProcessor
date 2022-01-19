from project.Connectors.DL.S3Connector import S3Connector
from project.DB.DataManagers.AbstractDataManager import AbstractDataManager
from project.DB.DataSerilazators.ChannelSerializator import ChannelSerializator
from project.DB.DataSerilazators.DateSerializator import DateSerializator
from project.DB.DataSerilazators.FactTableSerializer import FactTableSerializer
from project.DB.DataSerilazators.TimeSerializator import TimeSerializator
from project.DB.DataSerilazators.VideoSerializator import VideoSerializator
from project.DB.Loaders.AthenaS3.ChannelLoader import ChannelLoader
from project.DB.Loaders.AthenaS3.DateLoader import DateLoader
from project.DB.Loaders.AthenaS3.FactTableLoader import FactLoader
from project.DB.Loaders.AthenaS3.PFactTableLoader import PFactLoader
from project.DB.Loaders.AthenaS3.TimeLoader import TimeLoader
from project.DB.Loaders.AthenaS3.VideoLoader import VideoLoader


class AthenaDataManager(AbstractDataManager):
    def __init__(self):
        self.connector = S3Connector()

    def process_data(self, data, datetime):
        channel_serializator = ChannelSerializator()
        time_serializator = TimeSerializator()
        date_serializator = DateSerializator()
        video_serializator = VideoSerializator()
        fact_serializator = FactTableSerializer()

        time_json = time_serializator.serialize(datetime)
        date_json = date_serializator.serialize(datetime)
        channel_json = []
        video_json = []
        fact_json = []
        for channel in data:
            channel_json += [channel_serializator.serialize(channel)]
            for video in channel.videos:
                video_json += [video_serializator.serialize(video)]
                fact_json += [fact_serializator.serialize(video, date_json["id"], time_json["id"], channel.channel_id)]

        channel_loader = ChannelLoader(self.connector)
        video_loader = VideoLoader(self.connector)
        time_loader = TimeLoader(self.connector)
        date_loader = DateLoader(self.connector)
        fact_loader = FactLoader(self.connector)
        p_fact_loader = PFactLoader(self.connector)

        channel_loader.load(channel_json)
        video_loader.load(video_json)
        time_loader.load([time_json])
        date_loader.load([date_json])
        fact_loader.load(fact_json)
        p_fact_loader.load(fact_json)
