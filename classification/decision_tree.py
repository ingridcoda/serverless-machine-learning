from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier

import common as c


def run_decision_tree(num_folds=10, seed=7, test_size=0.25, dataset_name="iris", dataset_url=None):
    try:

        kfold = KFold(num_folds, True, random_state=seed)
        model = DecisionTreeClassifier()
        X, Y = c.load_dataset(dataset_name, dataset_url)
        X_training, X_test, Y_training, Y_test = c.split_dataset(test_size, seed, X, Y)

        print(f"Running CART decision tree by cross validation with {num_folds} folds and seed = {seed}:\n")
        c.training_and_evaluating_model_by_cross_validation(model, X, Y, kfold)
        print(f"\nRunning CART decision tree by training and tests partitions,"
              f" with seed = {seed} and {test_size * 100}% of test partition's size:\n")
        c.training_and_evaluating_model_by_training_and_test_partitions(model, X_training, X_test, Y_training, Y_test)

    except Exception as e:
        raise e
