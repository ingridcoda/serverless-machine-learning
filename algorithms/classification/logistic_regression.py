from sklearn.linear_model import LogisticRegression

import common as c


def run(num_folds, seed, test_size, dataset_name, dataset_url, solver, max_iter):
    try:
        model = LogisticRegression(solver=solver, max_iter=max_iter)
        c.run_with_regression_model(model, num_folds, seed, test_size, dataset_name, dataset_url)
    except Exception as e:
        raise e
