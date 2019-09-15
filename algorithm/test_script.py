from algorithm.dataset import Dataset

dataset = Dataset()
user_coords = [43.75, -79.45]
recommendations = dataset.get_recommendations(user_coords, 'Food and Dining', 0, 1, 2, 3, 4)
for e in recommendations:
    print(e)
