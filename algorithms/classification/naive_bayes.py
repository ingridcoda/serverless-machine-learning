from sklearn.naive_bayes import GaussianNB

import common as c


def run(num_folds, seed, test_size, dataset_url, delimiter):
    try:
        model = GaussianNB()
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_url, delimiter)
    except Exception as e:
        raise e
