import numpy as np

ATTRIBUTE_WEIGHTS = np.array([5, 4, 3, 2, 1])


class User:

    def __init__(self):
        self.attribute_values = np.array([1, 2, 3, 4, 5])
        self.norm_attribute_values = None
        self.establishment_visits = np.array([0.2, 0.1, 0.3, 0.4])

    def distance(self, other_user):
        return np.sum(ATTRIBUTE_WEIGHTS * np.square(self.norm_attribute_values - other_user.norm_attribute_values))
