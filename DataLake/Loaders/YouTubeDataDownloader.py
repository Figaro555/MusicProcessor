import json
import os

from Configs.YouTubeConfig import api_key, my_channels_id
from DataLake.Loaders.AbstractDownloader import AbstractDownloader

from googleapiclient.discovery import build


class YouTubeDataDownloader(AbstractDownloader):

    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.folder_to_store = ""

    def download_files(self, local_resource_path):
        self.folder_to_store = local_resource_path + "/YouTubeData/"

        if not os.path.exists(os.path.dirname(self.folder_to_store)):
            os.makedirs(os.path.dirname(self.folder_to_store))

        result_json = {}

        for channel_id in my_channels_id:
            request = self.youtube.channels().list(
                part='statistics, snippet, contentDetails',
                id=channel_id
            )
            response = request.execute()

            pl_request = self.youtube.playlistItems().list(
                part='contentDetails',
                playlistId=response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"],
                maxResults=5
            )
            pl_response = pl_request.execute()

            videos = {}
            for item in pl_response["items"]:
                v_request = self.youtube.videos().list(
                    part='statistics, snippet',
                    id=item["contentDetails"]["videoId"]
                )
                v_response = v_request.execute()

                videos[v_response["items"][0]['snippet']['title']] = {
                    "viewCount": v_response["items"][0]['statistics']['viewCount'],
                    "likeCount": v_response["items"][0]['statistics']['likeCount'],
                    "id": v_response["items"][0]['id']
                }

            result_json[response["items"][0]['snippet']['title']] = {
                "viewCount": response["items"][0]['statistics']['viewCount'],
                "videoCount": response["items"][0]['statistics']['videoCount'],
                "id": response["items"][0]['id'],
                "hiddenSubscriberCount": response["items"][0]['statistics']['hiddenSubscriberCount'],
                "videos": videos
            }
        s = json.dumps(result_json, indent=4, sort_keys=True, ensure_ascii=False)

        with open(self.folder_to_store + 'data.json', 'w', encoding='utf-8') as f:
            f.write(s)
