class Track:
    """Class that describes each line in file"""

    def __init__(self, identical_num, artist, song_name, duration, sections, segments):
        self.identical_num = identical_num
        self.artist = artist
        self.song_name = song_name
        self.duration = duration
        self.sections = sections
        self.segments = segments


