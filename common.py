import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split


def load_dataset(url, delimiter):
    dataset = pd.read_csv(url, skiprows=0, delimiter=delimiter)
    array = dataset.values
    last_column_index = len(dataset.columns) - 1
    x = array[:, 0:last_column_index]
    y = array[:, last_column_index]
    return x, y


def split_dataset(test_size, seed, data, target):
    return train_test_split(data, target, test_size=test_size, random_state=seed)


def report_metrics(data, predicts):
    print(classification_report(data, predicts))


def training_and_evaluating_model_by_cross_validation_for_classification(model, X, Y, kfold):
    result = cross_validate(model, X, Y, cv=kfold,
                            scoring=('accuracy', 'roc_auc'),
                            return_train_score=True)

    print(f"Training Accuracy: {((result['train_accuracy'].mean()) * 100)}%")
    print(f"Test Accuracy: {((result['test_accuracy'].mean()) * 100)}%")
    print(f"Training AUC: {((result['train_roc_auc'].mean()) * 100)}%")
    print(f"Test AUC: {((result['test_roc_auc'].mean()) * 100)}%\n")


def training_and_evaluating_model_by_training_and_test_partitions_for_classification(model, X_training, X_test,
                                                                                     Y_training, Y_test):
    trained_model = model.fit(X_training, Y_training)
    Y_predictions = trained_model.predict(X_test)
    right = (Y_test == Y_predictions).sum()
    total = Y_test.shape[0]

    print(f"Test Accuracy: {(right / total * 100)}%")
    print("Classification Report:")
    print(metrics.classification_report(Y_test, Y_predictions, zero_division=0))
    print("Confusion Matrix:")
    print(metrics.confusion_matrix(Y_test, Y_predictions), '\n\n')


def training_and_evaluating_model_by_cross_validation_for_regression(model, X, Y, kfold):
    result = cross_validate(model, X, Y, cv=kfold,
                            scoring=('neg_mean_squared_error', 'r2'),
                            return_train_score=True)

    print(f"Training RMSE: {np.sqrt(abs(result['train_neg_mean_squared_error'].mean()))}")
    print(f"Test RMSE: {np.sqrt(abs(result['test_neg_mean_squared_error'].mean()))}")
    print(f"Training MSE: {result['train_neg_mean_squared_error'].mean()}")
    print(f"Test MSE: {result['test_neg_mean_squared_error'].mean()}")
    print(f"Training R2: {result['train_r2'].mean()}")
    print(f"Test R2: {result['test_r2'].mean()}")


def training_and_evaluating_model_by_training_and_test_partitions_for_regression(model, X_training, X_test,
                                                                                 Y_training, Y_test):
    trained_model = model.fit(X_training, Y_training)
    Y_predictions = trained_model.predict(X_test)

    print(f"Test RMSE: {np.sqrt(metrics.mean_squared_error(Y_test, Y_predictions))}")
    print(f"Test MSE: {metrics.mean_squared_error(Y_test, Y_predictions)}")
    print(f"Test R2: {metrics.r2_score(Y_test, Y_predictions)}\n\n")


def prepare_to_run(num_folds, seed, test_size, dataset_url, delimiter):
    kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
    X, Y = load_dataset(dataset_url, delimiter)
    X_training, X_test, Y_training, Y_test = split_dataset(test_size, seed, X, Y)
    return X, Y, X_training, X_test, Y_training, Y_test, kfold


def run_with_classification_model(model, num_folds, seed, test_size, dataset_url, delimiter):
    X, Y, X_training, X_test, Y_training, Y_test, kfold = prepare_to_run(num_folds, seed, test_size,
                                                                         dataset_url, delimiter)
    print(f"Running model by cross validation:\n")
    training_and_evaluating_model_by_cross_validation_for_classification(model, X, Y, kfold)
    print(f"\nRunning model by training and tests partitions:\n")
    training_and_evaluating_model_by_training_and_test_partitions_for_classification(model, X_training, X_test,
                                                                                     Y_training, Y_test)


def run_with_regression_model(model, num_folds, seed, test_size, dataset_url, delimiter):
    X, Y, X_training, X_test, Y_training, Y_test, kfold = prepare_to_run(num_folds, seed, test_size,
                                                                         dataset_url, delimiter)
    print(f"Running model by cross validation:\n")
    training_and_evaluating_model_by_cross_validation_for_regression(model, X, Y, kfold)
    print(f"\nRunning model by training and tests partitions:\n")
    training_and_evaluating_model_by_training_and_test_partitions_for_regression(model, X_training, X_test,
                                                                                 Y_training, Y_test)


def run_with_grouping_model(model, dataset_url, delimiter):
    X, y = load_dataset(dataset_url, delimiter)
    predictions = model.fit_predict(X)
    distortion = model.inertia_
    print(f"Model predictions: {predictions}")
    print(f"Model distortion: {distortion}")
