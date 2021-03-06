import json

from project.Configs.YouTubeConfig import my_channels_id
from project.Connectors.DL.YouTubeConnector import YouTubeConnector
from project.DataLake.DataGetters.YouTube.ChannelDataGetter import ChannelDataGetter
from project.DataLake.DataGetters.YouTube.VideoDataGetter import VideoDataGetter
from project.DataLake.DataLoaders.AbstractDataLoader import AbstractDataLoader


class YouTubeDataLoader(AbstractDataLoader):
    def __init__(self):
        self.channel_getter = ChannelDataGetter()
        self.video_getter = VideoDataGetter()
        self.connector = YouTubeConnector()
        self.channel_ids = my_channels_id

    def save(self, resource_path):
        channels = self.channel_getter.get_data(self.channel_ids, self.connector)

        for channel in channels:
            channel["videos"] = self.video_getter.get_data(
                channel["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"],
                self.connector)

        result_json = {"root": channels
                       }
        s = json.dumps(result_json, indent=4, sort_keys=True, ensure_ascii=False)

        with open(resource_path + "/YouTubeData/" + 'data.json', 'w', encoding='utf-8') as f:
            f.write(s)
