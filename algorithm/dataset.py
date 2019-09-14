import json
import numpy as np
from algorithm.establishment import Establishment
from algorithm.user import User


EXAMPLE_USER_TRANSACTION = [{'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 53.01, 'desc': 'METRO #380', 'merch_name': 'Metro', 'date_time': '2018-10-12T09', 'lat_long': [43.719628844, -79.430367334], 'city': 'North York', 'country': 'CA', 'street': '3090 Bathurst St', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 5.94, 'desc': 'TIM HORTONS #892 _F', 'merch_name': 'Tim Hortons', 'date_time': '2018-10-12T10', 'lat_long': [43.6780979199, -79.4437273342], 'city': 'Toronto', 'country': 'CA', 'street': '1176 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 81.91, 'desc': 'CINEPLEX 9769', 'merch_name': 'Cineplex', 'date_time': '2018-10-12T17', 'lat_long': [43.6696411702, -79.3886879635], 'city': 'Toronto', 'country': 'CA', 'street': '55 Bloor St W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 52.01, 'desc': 'METRO #388', 'merch_name': 'Metro', 'date_time': '2018-10-05T11', 'lat_long': [43.708499534, -79.476926478], 'city': 'North York', 'country': 'CA', 'street': '1411 Lawrence Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 2.14, 'desc': 'TIM HORTONS #892 _F', 'merch_name': 'Tim Hortons', 'date_time': '2018-10-10T14', 'lat_long': [43.6780979199, -79.4437273342], 'city': 'Toronto', 'country': 'CA', 'street': '1176 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 4.89, 'desc': 'STARBUCKS #4540', 'merch_name': 'Starbucks', 'date_time': '2018-10-02T13', 'lat_long': [43.6814187349, -79.4258181307], 'city': 'Toronto', 'country': 'CA', 'street': '687 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 7.11, 'desc': 'STARBUCKS #4540', 'merch_name': 'Starbucks', 'date_time': '2018-10-03T11', 'lat_long': [43.6814187349, -79.4258181307], 'city': 'Toronto', 'country': 'CA', 'street': '687 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 3.89, 'desc': "MCDONALD'S #13612 QPS", 'merch_name': "McDonald's", 'date_time': '2018-10-11T08', 'lat_long': [43.6781876839, -79.4434299266], 'city': 'Toronto', 'country': 'CA', 'street': '1168 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 3.51, 'desc': "MCDONALD'S #13612 QPS", 'merch_name': "McDonald's", 'date_time': '2018-10-04T09', 'lat_long': [43.6781876839, -79.4434299266], 'city': 'Toronto', 'country': 'CA', 'street': '1168 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 1.81, 'desc': "MCDONALD'S #13612 QPS", 'merch_name': "McDonald's", 'date_time': '2018-10-16T12', 'lat_long': [43.6781876839, -79.4434299266], 'city': 'Toronto', 'country': 'CA', 'street': '1168 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 6.53, 'desc': 'STARBUCKS #4540', 'merch_name': 'Starbucks', 'date_time': '2018-10-05T18', 'lat_long': [43.6814187349, -79.4258181307], 'city': 'Toronto', 'country': 'CA', 'street': '687 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 43.85, 'desc': 'PETROCAN #97178', 'merch_name': 'Petro-Canada', 'date_time': '2018-10-15T12', 'lat_long': [43.7072936025, -79.4529210217], 'city': 'North York', 'country': 'CA', 'street': '2863 Dufferin St', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 5.76, 'desc': 'TIM HORTONS #892 _F', 'merch_name': 'Tim Hortons', 'date_time': '2018-10-09T16', 'lat_long': [43.6780979199, -79.4437273342], 'city': 'Toronto', 'country': 'CA', 'street': '1176 St Clair Ave W', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 49.71, 'desc': 'PETROCAN #05929', 'merch_name': 'Petro-Canada', 'date_time': '2018-10-01T14', 'lat_long': [43.6806188086, -79.4754016734], 'city': 'York', 'country': 'CA', 'street': '385 Weston Rd', 'region': 'ON'}, {'customer': '45a3a79a-e39c-4310-8ad2-7a21ac3c5e53', 'amount': 26.2, 'desc': 'PETROCAN #05929', 'merch_name': 'Petro-Canada', 'date_time': '2018-10-08T09', 'lat_long': [43.6806188086, -79.4754016734], 'city': 'York', 'country': 'CA', 'street': '385 Weston Rd', 'region': 'ON'}]


class Dataset:

    def __init__(self):
        self.establishments = []
        with open('/Users/brendon/Downloads/td_transaction_2018-10.json') as transaction_file:
            transactions_nested = list(json.load(transaction_file).values())
        transactions = []
        for sublist in transactions_nested:
            transactions.extend(sublist)

        transactions_by_user = {}
        self.establishment_indices_by_tag = {}
        for transaction in transactions:
            transaction['tag'] = 'example_tag'
            user_id = transaction['customer']
            if user_id not in transactions_by_user:
                transactions_by_user[user_id] = []
            transactions_by_user[user_id].append(transaction)
            establishment_id = transaction['desc']
            if establishment_id not in [establishment.establishment_id for establishment in self.establishments]:
                self.establishments.append(Establishment(establishment_id, transaction['lat_long'], transaction['tag']))

        self.establishment_ids = [establishment.establishment_id for establishment in self.establishments]
        self.users = [User(transactions_by_user[key], self.establishment_ids) for key in transactions_by_user]
        self.combined_attribute_values = np.stack([user.attribute_values for user in self.users])
        mean = np.mean(self.combined_attribute_values)
        std_dev = np.std(self.combined_attribute_values)
        if std_dev == 0.0:
            std_dev = 1.0
        for user in self.users:
            user.norm_attribute_values = (user.attribute_values - mean) / std_dev

    def get_recommendations(self, user_coords, num_recommendations, tag, slider_value_1, slider_value_2):
        for w in EXAMPLE_USER_TRANSACTION:
            w['tag'] = 'example_tag'

        user = User(EXAMPLE_USER_TRANSACTION, self.establishment_ids)
        mean = np.mean(self.combined_attribute_values)
        std_dev = np.std(self.combined_attribute_values)
        if std_dev == 0.0:
            std_dev = 1.0
        user.norm_attribute_values = (user.attribute_values - mean) / std_dev

        establishment_visits = self.weighted_establishments(user)
        for i in range(len(self.establishments)):
            d = self.establishments[i].distance_km(user_coords)
            if self.establishments[i].distance_km(user_coords) > 3:
                establishment_visits[i] = -1
            if self.establishments[i].tag != tag:
                establishment_visits[i] = -1
        indices = np.flip(np.argsort(establishment_visits))
        best_establishments = [self.establishments[i] for i in indices[:num_recommendations]]
        return best_establishments

    def weighted_establishments(self, user):
        weighted_establishment_visits = np.zeros(user.establishment_visits.shape)
        for other_user in self.users:
            distance = user.distance(other_user)
            weight = 1 / (distance + 0.1)
            weighted_establishment_visits += weight * other_user.establishment_visits
        weighted_establishment_visits /= np.sum(weighted_establishment_visits)
        return weighted_establishment_visits
