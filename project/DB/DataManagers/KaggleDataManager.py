from project.Connectors.DB.PostgresConnector import PostgresConnector
from project.DB.DataManagers.AbstractDataManager import AbstractDataManager
from project.DB.Loaders.Kaggle.SectionLoader import SectionLoader
from project.DB.Loaders.Kaggle.SegmentLoader import SegmentLoader
from project.DB.Loaders.Kaggle.TrackLoader import TrackLoader


class KaggleDataManager(AbstractDataManager):
    def __init__(self):
        self.connector = PostgresConnector()
        self.track_loader = TrackLoader(self.connector)
        self.segment_loader = SegmentLoader(self.connector)
        self.section_loader = SectionLoader(self.connector)

    def process_data(self, data):
        for track in data:
            track_id = self.track_loader.load(track)
            for segment in track.segments:
                self.segment_loader.load(segment, track_id)
            for section in track.sections:
                self.section_loader.load(section, track_id)
