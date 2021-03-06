from sklearn.tree import DecisionTreeClassifier

import common as c


def run(num_folds, seed, test_size, dataset_url, delimiter, criterion, max_depth):
    try:
        model = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth)
        c.run_with_classification_model(model, num_folds, seed, test_size, dataset_url, delimiter)
    except Exception as e:
        raise e
