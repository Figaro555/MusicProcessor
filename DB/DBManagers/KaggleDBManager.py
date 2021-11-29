from DB.Connectors.PostgresConnector import PostgresConnector
from DB.DBManagers.AbstractDBManager import AbstractDBManager
from DB.Initializers.Kaggle.KaggleInitializer import KaggleInitializer
from DB.Loaders.Kaggle.SectionLoader import SectionLoader
from DB.Loaders.Kaggle.SegmentLoader import SegmentLoader
from DB.Loaders.Kaggle.TrackLoader import TrackLoader


class KaggleDBManager(AbstractDBManager):
    def __init__(self):
        self.connector = PostgresConnector()
        self.initializer = KaggleInitializer()
        self.track_loader = TrackLoader(self.connector)
        self.segment_loader = SegmentLoader(self.connector)
        self.section_loader = SectionLoader(self.connector)

        self.initializer.create_tables(self.connector)

    def process_data(self, data):
        for track in data:
            track_id = self.track_loader.load(track)
            for segment in track.segments:
                self.segment_loader.load(segment, track_id)
            for section in track.sections:
                self.section_loader.load(section, track_id)
