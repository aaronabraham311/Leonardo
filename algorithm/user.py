ATTRIBUTE_WEIGHTS = [5, 4, 3, 2, 1]


class User:
    def __init__(self):
        self.attribute_values = [1, 2, 3, 4, 5]

    def distance(self, other_user):
        return sum(ATTRIBUTE_WEIGHTS[i] * ((self.attribute_values[i] - other_user.attribute_values[i]) ** 2) for i in range(len(ATTRIBUTE_WEIGHTS)))
