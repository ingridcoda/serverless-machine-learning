from sklearn.neighbors import KNeighborsClassifier

import common as c


def run(num_folds, seed, test_size, dataset_url, delimiter, k, distance_type):
    try:
        model = KNeighborsClassifier(n_neighbors=k, metric=distance_type)
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_url, delimiter)
    except Exception as e:
        raise e
