import json
import unittest
from unittest import main, TestCase

from project.Transformers.Kaggle.TestsOnDataTransformer import TestsOnDataTransformer
from project.Entities.Kaggle.TestsOnData.Track import Track
from project.Entities.Kaggle.TestsOnData.Segment import Segment
from project.Entities.Kaggle.TestsOnData.Section import Section


class KaggleTestsOnDataTransformerTest(TestCase):

    def setUp(self):
        file = open('KaggleTest.json', "r", encoding="utf-8")
        self.parsed_json = json.load(file)
        file.close()
        self.tt = TestsOnDataTransformer()
        unittest.main(exit=False)

    def test_transform_to_local_array_length_checker(self):
        result = self.tt.transform_to_local_array(self.parsed_json)

        self.assertEqual(len(result), 1)

    def test_transform_to_local_array_empty_list_checker(self):
        result = self.tt.transform_to_local_array([])

        self.assertEqual(result, [])

    def test_transform_to_local_array_segments_length_checker(self):
        result = self.tt.transform_to_local_array(self.parsed_json)

        self.assertEqual(len(result[0].segments), 3)

    def test_transform_to_local_array_sections_length_checker(self):
        result = self.tt.transform_to_local_array(self.parsed_json)

        self.assertEqual(len(result[0].sections), 2)

    def test_transform_to_local_array_track_type(self):
        result = self.tt.transform_to_local_array(self.parsed_json)
        self.assertTrue(type(result[0]) is Track)

    def test_transform_to_local_array_segment_type(self):
        result = self.tt.transform_to_local_array(self.parsed_json)
        self.assertTrue(type(result[0].segments[0]) is Segment)

    def test_transform_to_local_array_section_type(self):
        result = self.tt.transform_to_local_array(self.parsed_json)
        self.assertTrue(type(result[0].sections[0]) is Section)

    def test_transform_to_local_array_comparing_full_result(self):
        result = self.tt.transform_to_local_array(self.parsed_json)
        expected_result = Track(
            identical_num='spotify:track:5gICNh1EHmDlpyWERFitXG',
            artist='Southern Avenue',
            song_name='Savior',
            duration=223.49048,
            sections=[Section(duration=36.15176,
                              loudness=-8.416,
                              start=0.0
                              ),
                      Section(duration=42.0297,
                              loudness=-3.606,
                              start=36.15176
                              )],
            segments=[Segment(duration=0.12163,
                              loudness_max=-60.0,
                              loudness_max_time=0.0,
                              loudness_start=-60.0,
                              start=0.0
                              ),
                      Segment(duration=0.55129,
                              loudness_max=-9.87,
                              loudness_max_time=0.25127,
                              loudness_start=-60.0,
                              start=0.12163
                              ),
                      Segment(duration=0.39628,
                              loudness_max=-18.931,
                              loudness_max_time=0.02625,
                              loudness_start=-23.007,
                              start=0.67293
                              )
                      ]
        )

        self.assertTrue(
            result,
            expected_result
        )

    def test_transform_to_local_array_failure(self):
        self.assertRaises(TypeError, self.tt.transform_to_local_array, 2)


if __name__ == '__main__':
    main()
