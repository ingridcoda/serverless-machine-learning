from sklearn.neighbors import KNeighborsClassifier

import common as c


def run(num_folds, seed, test_size, dataset_name, dataset_url, k, distance_type):
    try:
        model = KNeighborsClassifier(n_neighbors=k, metric=distance_type)
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_name, dataset_url)
    except Exception as e:
        raise e
