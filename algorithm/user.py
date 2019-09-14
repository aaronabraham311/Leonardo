import numpy as np

ATTRIBUTE_WEIGHTS = np.array([1])

TAGS = ['example_tag']


class User:

    def __init__(self, transactions, establishment_ids, account):
        self.establishment_visits = np.zeros(len(establishment_ids))
        total_expenditure = sum(transaction['amount'] for transaction in transactions)
        expenditure_by_tag = {}
        for transaction in transactions:
            establishment_id = transaction['desc']
            index = establishment_ids.index(establishment_id)
            self.establishment_visits[index] += 1

            tag = transaction['tag']
            if tag not in expenditure_by_tag:
                expenditure_by_tag[tag] = 0
            expenditure_by_tag[tag] += transaction['amount']

        values_in_order = []
        for tag in TAGS:
            if tag in expenditure_by_tag:
                values_in_order.append(expenditure_by_tag[tag])
            else:
                values_in_order.append(0.0)
        normalized_values = [value / total_expenditure for value in values_in_order]
        income = account['income']
        self.attribute_values = np.array(normalized_values + [income])

        self.establishment_visits /= np.sum(self.establishment_visits)
        self.norm_attribute_values = None

    def distance(self, other_user):
        return np.sum(ATTRIBUTE_WEIGHTS * np.square(self.norm_attribute_values - other_user.norm_attribute_values))
