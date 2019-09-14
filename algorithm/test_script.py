from algorithm.dataset import Dataset

dataset = Dataset()
user_coords = [43.75, -79.45]
recommendations = dataset.get_recommendations(user_coords, 5, 'example_tag', 0, 1)
for e in recommendations:
    print(e.distance_km(user_coords))
