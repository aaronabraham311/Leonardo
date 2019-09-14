import json
import numpy as np
from algorithm.establishment import Establishment
from algorithm.user import User


class Dataset:

    def __init__(self):
        with open('/Users/brendon/Downloads/td_accounts.json') as account_file:
            accounts_nested = json.load(account_file)
        accounts = [accounts_nested[key] for key in accounts_nested]

        with open('/Users/brendon/Downloads/td_transaction_2018-10.json') as transaction_file:
            transactions_nested = list(json.load(transaction_file).values())
        transactions = []
        for sublist in transactions_nested:
            transactions.extend(sublist)

        transactions_by_user = {}
        transactions_by_establishment = {}
        accounts_by_user_id = {}
        self.establishment_indices_by_tag = {}
        for transaction in transactions:
            transaction['tag'] = 'example_tag'
            user_id = transaction['customer']
            for account in accounts:
                if account['cust_id'] == user_id:
                    accounts_by_user_id[user_id] = account
            if user_id not in transactions_by_user:
                transactions_by_user[user_id] = []
            transactions_by_user[user_id].append(transaction)
            establishment_id = transaction['desc']
            if establishment_id not in transactions_by_establishment:
                transactions_by_establishment[establishment_id] = []
            transactions_by_establishment[establishment_id].append(transaction)

        self.establishments = []
        for establishment_id in transactions_by_establishment:
            self.establishments.append(Establishment(establishment_id, transactions_by_establishment[establishment_id][0]['lat_long'], transaction['tag'], transactions_by_establishment[establishment_id]))

        self.establishment_ids = [establishment.establishment_id for establishment in self.establishments]
        self.users = [User(transactions_by_user[key], self.establishment_ids, accounts_by_user_id[key]) for key in transactions_by_user]
        self.combined_attribute_values = np.stack([user.attribute_values for user in self.users if None not in user.attribute_values])
        self.norm_mean = np.mean(self.combined_attribute_values, axis=0)
        self.norm_std_dev = np.std(self.combined_attribute_values)
        if self.norm_std_dev == 0.0:
            self.norm_std_dev = 1.0
        for user in self.users:
            try:
                user.norm_attribute_values = (user.attribute_values - self.norm_mean) / self.norm_std_dev
            except TypeError:
                user.norm_attribute_values = None

    def get_recommendations(self, user, user_coords, num_recommendations, tag, slider_value_1, slider_value_2):
        establishment_visits = self.weighted_establishments(user)
        for i in range(len(self.establishments)):
            if self.establishments[i].distance_km(user_coords) > 5:
                establishment_visits[i] = -1
            if self.establishments[i].tag != tag:
                establishment_visits[i] = -1
        indices = np.flip(np.argsort(establishment_visits))
        best_establishments = [self.establishments[i] for i in indices[:num_recommendations]]
        return best_establishments

    def weighted_establishments(self, user):
        weighted_establishment_visits = np.zeros(user.establishment_visits.shape)
        for other_user in self.users:
            if other_user.norm_attribute_values is None:
                continue
            distance = user.distance(other_user)
            weight = 1 / (distance + 0.1)
            weighted_establishment_visits += weight * other_user.establishment_visits
        weighted_establishment_visits /= np.sum(weighted_establishment_visits)
        return weighted_establishment_visits
