class Segment:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Segment):
            return (self.start == o.start and
                    self.duration == o.duration and
                    self.loudness_max == o.loudness_max and
                    self.loudness_max_time == o.loudness_max_time and
                    self.loudness_start ==o.loudness_start)

        return False

    def __init__(self, start, duration, loudness_start, loudness_max_time, loudness_max):
        self.start = start
        self.duration = duration
        self.loudness_start = loudness_start
        self.loudness_max_time = loudness_max_time
        self.loudness_max = loudness_max
