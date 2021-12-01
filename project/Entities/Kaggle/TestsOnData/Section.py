class Section:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Section):
            return (self.start == o.start and
                    self.duration == o.duration and
                    self.loudness == o.loudness)

        return False

    def __init__(self, start, duration, loudness):
        self.start = start
        self.duration = duration
        self.loudness = loudness
