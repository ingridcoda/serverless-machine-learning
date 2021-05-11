from sklearn.svm import SVC

import common as c


def run(num_folds, seed, test_size, dataset_url, delimiter, _c, gamma, kernel):
    try:
        model = SVC(C=_c, gamma=gamma, kernel=kernel)
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_url, delimiter)
    except Exception as e:
        raise e
