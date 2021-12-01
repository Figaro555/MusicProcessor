class Track:
    """Class that describes each line in file"""

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Track):
            return (self.duration == o.duration and
                    self.artist == o.artist and
                    self.song_name == o.song_name and
                    self.duration == o.duration and
                    self.sections == o.sections and
                    self.segments == o.segments)

        return False

    def __init__(self, identical_num, artist, song_name, duration, sections, segments):
        self.identical_num = identical_num
        self.artist = artist
        self.song_name = song_name
        self.duration = duration
        self.sections = sections
        self.segments = segments
