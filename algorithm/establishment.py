import numpy as np


class Establishment:

    def __init__(self, establishment_id, coords_list, tag, transactions):
        self.establishment_id = establishment_id
        self.coords = np.array(coords_list)
        self.tag = tag
        self.mean_amount = np.mean([transaction['amount'] for transaction in transactions])

    def distance_km(self, other_coords):
        self_lat, self_long = np.deg2rad(self.coords)
        other_lat, other_long = np.deg2rad(other_coords)
        a = 0.5 - np.cos(other_lat - self_lat) / 2 + np.cos(self_lat) * np.cos(other_lat) * (1 - np.cos(other_long - self_long)) / 2
        earth_diameter = 12742
        return earth_diameter * np.arcsin(np.sqrt(a))
