import json
import unittest
from unittest import main, TestCase

from project.Transformers.YouTubeTransformer import YouTubeTransformer
from project.Entities.YouTubeData.Channel import Channel
from project.Entities.YouTubeData.Video import Video


class YouTubeTransformerTest(TestCase):

    def setUp(self):
        file = open('YouTubeTest.json', "r", encoding="utf-8")
        self.parsed_json = json.load(file)
        file.close()
        self.yt = YouTubeTransformer()
        unittest.main(exit=False)

    def test_transform_to_local_array_length_checker(self):
        result = self.yt.transform_to_local_array(self.parsed_json["root"])

        self.assertEqual(len(result), 2)

    def test_transform_to_local_array_empty_list_checker(self):
        result = self.yt.transform_to_local_array([])

        self.assertEqual(result, [])

    def test_transform_to_local_array_video_length_checker(self):
        result = self.yt.transform_to_local_array(self.parsed_json["root"])

        self.assertEqual(len(result[0].videos), 3)

    def test_transform_to_local_array_channel_type(self):
        result = self.yt.transform_to_local_array(self.parsed_json["root"])
        self.assertTrue(type(result[0]) is Channel)

    def test_transform_to_local_array_video_type(self):
        result = self.yt.transform_to_local_array(self.parsed_json["root"])
        self.assertTrue(type(result[0].videos[0]) is Video)


if __name__ == '__main__':
    main()
