from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator
from project.Entities.YouTubeData.Video import Video


class FactTableSerializer(AbstractDataSerializator):
    def serialize(self, video: Video, date_id, time_id, channel_id):
        return {"video_id": video.video_id, "channel_id": channel_id, "date_id": date_id,
                "time_id": time_id, "view_count": int(video.view_count), "like_count": int(video.like_count)}
