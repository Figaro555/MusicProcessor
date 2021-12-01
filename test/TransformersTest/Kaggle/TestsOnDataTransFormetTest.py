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


if __name__ == '__main__':
    main()
