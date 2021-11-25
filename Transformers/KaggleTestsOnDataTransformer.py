from Enteties.KaggleTestsOnData.Track import Track
from Enteties.KaggleTestsOnData.Section import Section
from Enteties.KaggleTestsOnData.Segment import Segment
from Transformers.AbstractTransformer import AbstractTransformer


class KaggleTestsOnDataTransformer(AbstractTransformer):

    def transform_to_local_array(self, local_dl):
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
