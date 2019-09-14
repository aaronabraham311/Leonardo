import numpy as np

from algorithm.establishment import Establishment
from algorithm.user import User


class Dataset:

    def __init__(self):
        self.establishments = [Establishment(), Establishment(), Establishment(), Establishment()]
        self.users = [User(), User(), User(), User(), User(), User()]
        combined_attribute_values = np.stack([user.attribute_values for user in self.users])
        mean = np.mean(combined_attribute_values)
        std_dev = np.std(combined_attribute_values)
        for user in self.users:
            user.norm_attribute_values = (user.attribute_values - mean) / std_dev

    def get_recommendations(self, user_coords, num_recommendations, slider_value_1, slider_value_2):
        user = User()
        establishment_visits = self.weighted_establishments(user)
        for i in range(len(self.establishments)):
            if self.establishments[i].distance(user_coords) > 1:
                establishment_visits[i] = -1
        indices = np.flip(np.argsort(establishment_visits))
        best_establishments = [self.establishments[i] for i in indices[:num_recommendations]]
        return best_establishments

    def weighted_establishments(self, user):
        weighted_establishment_visits = np.zeros(user.establishment_visits.shape)
        for other_user in self.users:
            distance = user.distance(other_user)
            weight = 1 / distance
            weighted_establishment_visits += weight * other_user.establishment_visits
        weighted_establishment_visits /= np.sum(weighted_establishment_visits)
        return weighted_establishment_visits
