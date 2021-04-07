import json

import decision_tree
import knn
import logistic_regression
import naive_bayes
import svm
from exceptions import *


def handler(event, context):
    try:
        algorithm = event.get("algorithm", None)
        kfold = event.get("kfold", 10)
        seed = event.get("seed", 7)
        test_size = event.get("test_size", 0.25)
        dataset_name = event.get("dataset_name", "iris")
        dataset_url = event.get("dataset_url", None)

        print("Parameters values:\n")
        print(f" - Algorithm type: {algorithm}")
        print(f" - Dataset: {dataset_url if dataset_url else dataset_name}")
        print(f" - Number of folds: {kfold}")
        print(f" - Seed: {seed}")
        print(f" - Test size: {test_size}")

        if not event or not algorithm:
            raise BadRequestException("400 - Parameter 'algorithm' is required.")

        elif "decision_tree" in algorithm:
            print("\nRunning decision tree algorithm...")
            decision_tree.run(kfold, seed, test_size, dataset_name, dataset_url)
            print("Decision tree algorithm was completed successful!\n")

        elif "knn" in algorithm:
            k = event.get("k", 10)
            distance_type = event.get("distance_type", "euclidean")
            print(f" - Number of neighbors: {k}")
            print(f" - Distance type: {distance_type}")
            print("\nRunning KNN algorithm...")
            knn.run(kfold, seed, test_size, dataset_name, dataset_url, k, distance_type)
            print("KNN algorithm was completed successful!\n")

        elif "naive_bayes" in algorithm:
            print("\nRunning Naive Bayes algorithm...")
            naive_bayes.run(kfold, seed, test_size, dataset_name, dataset_url)
            print("Naive Bayes algorithm was completed successful!\n")

        elif "svm" in algorithm:
            gamma = event.get("gamma", "auto")
            kernel = event.get("kernel", "rbf")
            print(f" - Gamma: {gamma}")
            print(f" - Kernel type: {kernel}")
            print("\nRunning SVM algorithm...")
            svm.run(kfold, seed, test_size, dataset_name, dataset_url, gamma, kernel)
            print("SVM algorithm was completed successful!\n")

        elif "logistic_regression" in algorithm:
            solver = event.get("solver", "lbfgs")
            print(f" - Solver type: {solver}")
            print("\nRunning Logistic Regression algorithm...")
            logistic_regression.run(kfold, seed, test_size, dataset_name, dataset_url, solver)
            print("Logistic Regression algorithm was completed successful!\n")

        else:
            raise BadRequestException("400 - Algorithm type was invalid or not given! "
                                      "Please, choose one of these options: "
                                      "['decision_tree', 'knn', 'naive_bayes', 'svm', 'logistic_regression'].")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "Message": "Success!"
            })
        }

    except BadRequestException as e:
        raise e

    except Exception as e:
        raise UnknownException("500 - Unexpected error.", e)


if __name__ == "__main__":
    handler({}, '')
