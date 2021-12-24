from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator
from project.Entities.YouTubeData.Video import Video


class VideoSerializator(AbstractDataSerializator):
    def serialize(self, video: Video):
        return {"id": video.video_id, "title": video.title}
