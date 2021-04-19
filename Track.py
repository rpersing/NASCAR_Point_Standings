class Track:
    def __init__(self, track_brand, track_name, track_laps, track_miles):
        self.track_brand = track_brand
        self.track_name = track_name
        self.track_laps = track_laps
        self.track_miles = track_miles

    def get_track_brand(self):
        return self.track_brand

    def get_track_name(self):
        return self.track_name

    def get_track_laps(self):
        return self.track_laps

    def get_track_miles(self):
        return self.track_miles
