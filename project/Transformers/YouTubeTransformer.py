from project.Entities.YouTubeData.Video import Video
from project.Entities.YouTubeData.Channel import Channel
from project.Transformers.AbstractTransformer import AbstractTransformer


class YouTubeTransformer(AbstractTransformer):

    def transform_to_local_array(self, local_dl):
        if not hasattr(local_dl, '__iter__'):
            raise TypeError("object is not iterable")

        return [Channel(channel["items"][0]["id"],
                        channel["items"][0]["snippet"]["title"],
                        channel["items"][0]["statistics"]["videoCount"],
                        channel["items"][0]["statistics"]["viewCount"],
                        channel["items"][0]["statistics"]["hiddenSubscriberCount"],

                        [Video(video["items"][0]["id"],
                               video["items"][0]["snippet"]["title"],
                               video["items"][0]["statistics"]["likeCount"],
                               video["items"][0]["statistics"]["viewCount"]
                               )
                         for video in channel["videos"]]
                        )
                for channel in local_dl]
