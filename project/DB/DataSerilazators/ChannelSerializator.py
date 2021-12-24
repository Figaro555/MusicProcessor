from project.DB.DataSerilazators.AbstractDataSerializator import AbstractDataSerializator
from project.Entities.YouTubeData.Channel import Channel


class ChannelSerializator(AbstractDataSerializator):
    def serialize(self, channel: Channel):
        return {"id": channel.channel_id, "title": channel.title, "video_count": channel.video_count,
                "view_count": channel.view_count, "description": channel.description}
