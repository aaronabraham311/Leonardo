from algorithm.dataset import Dataset

dataset = Dataset()
user = dataset.users[0]
user.attribute_values[1] = 80000
user.norm_attribute_values = (user.attribute_values - dataset.norm_mean) / dataset.norm_std_dev
user_coords = [43.75, -79.45]
recommendations = dataset.get_recommendations(user, user_coords, 5, 'example_tag', 0, 1)
for e in recommendations:
    print(e.establishment_id, e.mean_amount)
