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

    def test_transform_to_local_array_comparing_full_result(self):
        result = self.yt.transform_to_local_array(self.parsed_json["root"])
        expected_result = Channel(channel_id='UCsK1oV0PGkcZ1UhFtajx0dg',
                                  hidden_subscriber_count=False,
                                  title='Redroom',
                                  video_count='242',
                                  view_count='76260162',
                                  videos=[
                                      Video(like_count='5587',
                                            title='Клеопатра - последняя царица Древнего Египта',
                                            video_id='Nft7eSj7j30',
                                            view_count='40685'),
                                      Video(like_count='16426',
                                            title='Марокко: империя, которая (не) смогла',
                                            video_id='Ptqms7jwuMg',
                                            view_count='161648'),
                                      Video(like_count='15517',
                                            title='Шри Ланка: гражданская война и терроризм на райском острове. Тигры освобождения Тамил-Илама',
                                            video_id='0QxP8LwHEfw',
                                            view_count='172180')
                                  ]
                                  )
        self.assertTrue(
            result[0],
            expected_result
        )

    def test_transform_to_local_array_failure(self):
        self.assertRaises(TypeError, self.yt.transform_to_local_array, 2)

    if __name__ == '__main__':
        main()
