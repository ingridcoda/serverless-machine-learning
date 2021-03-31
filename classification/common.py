import pandas as pd
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split


def load_dataset(name, url):
    x = None
    y = None

    if url:
        dataset = pd.read_csv(url, skiprows=0, delimiter=',')
        array = dataset.values
        x = array[:, 0:8]
        y = array[:, 8]

    elif name == 'iris':
        dataset = load_iris()
        x = dataset.data[:, :2]
        y = dataset.target

    return x, y


def split_dataset(test_size, seed, data, target):
    return train_test_split(data, target, test_size=test_size, random_state=seed)


def report_metrics(data, predicts):
    print(classification_report(data, predicts))


def training_and_evaluating_model_by_cross_validation(model, X, Y, kfold):
    result = cross_validate(model, X, Y, cv=kfold,
                            scoring=('accuracy', 'roc_auc'),
                            return_train_score=True)

    print(f"Training Accuracy: {((result['train_accuracy'].mean()) * 100)}%")
    print(f"Test Accuracy: {((result['test_accuracy'].mean()) * 100)}%")
    print(f"Training AUC: {((result['train_roc_auc'].mean()) * 100)}%")
    print(f"Test AUC: {((result['test_roc_auc'].mean()) * 100)}%\n")


def training_and_evaluating_model_by_training_and_test_partitions(model, X_training, X_test, Y_training, Y_test):
    trained_model = model.fit(X_training, Y_training)
    Y_predictions = trained_model.predict(X_test)
    right = (Y_test == Y_predictions).sum()
    total = Y_test.shape[0]

    print(f"Test Accuracy: {(right / total * 100)}%")
    print("Classification Report:")
    print(metrics.classification_report(Y_test, Y_predictions))
    print("Confusion Matrix:")
    print(metrics.confusion_matrix(Y_test, Y_predictions), '\n\n')
