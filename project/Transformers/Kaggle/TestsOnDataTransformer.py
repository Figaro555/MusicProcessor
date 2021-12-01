from project.Entities.Kaggle.TestsOnData.Track import Track
from project.Entities.Kaggle.TestsOnData.Section import Section
from project.Entities.Kaggle.TestsOnData.Segment import Segment
from project.Transformers.AbstractTransformer import AbstractTransformer


class TestsOnDataTransformer(AbstractTransformer):

    def transform_to_local_array(self, local_dl):
        if not hasattr(local_dl, '__iter__'):
            raise TypeError("object is not iterable")

        return [Track(key,
                      local_dl[key]["artist"],
                      local_dl[key]["song"],
                      local_dl[key]["meta"]["track"][
                          "duration"],
                      [Section(section["start"],
                               section["duration"],
                               section["loudness"])
                       for section in
                       local_dl[key]["meta"]["sections"]],
                      [Segment(segment["start"],
                               segment["duration"],
                               segment["loudness_start"],
                               segment["loudness_max_time"],
                               segment["loudness_max"]
                               )
                       for segment in
                       local_dl[key]["meta"]["segments"]]

                      )
                for key in local_dl]
