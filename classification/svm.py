from sklearn.svm import SVC

import common as c


def run(num_folds, seed, test_size, dataset_name, dataset_url, gamma, kernel):
    try:
        model = SVC(gamma=gamma, kernel=kernel)
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_name, dataset_url)
    except Exception as e:
        raise e
