from Entities.YouTubeData.Video import Video
from Entities.YouTubeData.Channel import Channel
from Transformers.AbstractTransformer import AbstractTransformer


class YouTubeTransformer(AbstractTransformer):

    def transform_to_local_array(self, local_dl):
        return [Channel(local_dl[key]["id"],
                        key,
                        local_dl[key]["videoCount"],
                        local_dl[key]["viewCount"],
                        local_dl[key]["hiddenSubscriberCount"],
                        [Video(local_dl[key]["videos"][video]["id"],
                               video,
                               local_dl[key]["videos"][video]["likeCount"],
                               local_dl[key]["videos"][video]["viewCount"]
                               )
                         for video in
                         local_dl[key]["videos"].keys()]

                        )
                for key in local_dl.keys()]
