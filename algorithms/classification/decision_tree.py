from sklearn.tree import DecisionTreeClassifier

import common as c


def run(num_folds, seed, test_size, dataset_name, dataset_url):
    try:
        model = DecisionTreeClassifier()
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_name, dataset_url)
    except Exception as e:
        raise e
