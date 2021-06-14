import json

from algorithms.classification import (naive_bayes, decision_tree, svm, knn, logistic_regression)
from algorithms.grouping import (k_means)
from exceptions import (BadRequestException, UnknownException)


def handler(event, context):
    supported_types = ['classification', 'grouping']
    supported_classification_algorithms = ['decision_tree', 'knn', 'naive_bayes', 'svm', 'logistic_regression']
    supported_grouping_algorithms = ['k_means']

    try:
        _type = event.get("type", None)
        algorithm = event.get("algorithm", None)
        dataset_url = event.get("dataset_url", None)
        delimiter = event.get("delimiter", ",")

        if not event or not _type:
            raise BadRequestException("400 - Parameter 'type' is required.")

        elif _type not in supported_types:
            raise BadRequestException("400 - Model type was invalid or not given! "
                                      f"Please, choose one of these options: {supported_types}.")

        elif not algorithm:
            raise BadRequestException("400 - Parameter 'algorithm' is required.")

        elif not dataset_url:
            raise BadRequestException("400 - Parameter 'dataset_url' is required.")

        print("Parameters values:\n")
        print(f" - Model type: {_type}")
        print(f" - Algorithm: {algorithm}")
        print(f" - Dataset: {dataset_url}")
        print(f" - Dataset delimiter: {delimiter}")

        if _type == "classification":
            kfold = event.get("kfold", 10)
            seed = event.get("seed", 7)
            test_size = event.get("test_size", 0.25)

            print(f" - Number of folds: {kfold}")
            print(f" - Seed: {seed}")
            print(f" - Test size: {test_size}")

            if algorithm not in supported_classification_algorithms:
                raise BadRequestException("400 - Algorithm was invalid or not given! "
                                          f"Please, choose one of these options: "
                                          f"{supported_classification_algorithms}.")

            elif "decision_tree" in algorithm:
                criterion = event.get("criterion", "gini")
                max_depth = event.get("max_depth", None)

                print(f" - Criterion: {criterion}")
                print(f" - Maximum depth: {max_depth}")

                print("\nRunning decision tree algorithm...")
                decision_tree.run(kfold, seed, test_size, dataset_url, delimiter, criterion, max_depth)
                print("Decision tree algorithm was completed successful!\n")

            elif "knn" in algorithm:
                k = event.get("k", 10)
                distance_type = event.get("distance_type", "euclidean")

                print(f" - Number of neighbors: {k}")
                print(f" - Distance type: {distance_type}")

                print("\nRunning KNN algorithm...")
                knn.run(kfold, seed, test_size, dataset_url, delimiter, k, distance_type)
                print("KNN algorithm was completed successful!\n")

            elif "naive_bayes" in algorithm:
                print("\nRunning Naive Bayes algorithm...")
                naive_bayes.run(kfold, seed, test_size, dataset_url, delimiter)
                print("Naive Bayes algorithm was completed successful!\n")

            elif "svm" in algorithm:
                c = event.get("C", 1.0)
                gamma = event.get("gamma", "auto")
                kernel = event.get("kernel", "rbf")

                print(f" - C: {c}")
                print(f" - Gamma: {gamma}")
                print(f" - Kernel type: {kernel}")

                print("\nRunning SVM algorithm...")
                svm.run(kfold, seed, test_size, dataset_url, delimiter, c, gamma, kernel)
                print("SVM algorithm was completed successful!\n")

            elif "logistic_regression" in algorithm:
                solver = event.get("solver", "lbfgs")
                max_iter = event.get("max_iter", 1000)

                print(f" - Solver type: {solver}")
                print(f" - Maximum of iterations: {max_iter}")

                print("\nRunning Logistic Regression algorithm...")
                logistic_regression.run(kfold, seed, test_size, dataset_url, delimiter, solver, max_iter)
                print("Logistic Regression algorithm was completed successful!\n")

        elif _type == "grouping":
            if algorithm not in supported_grouping_algorithms:
                raise BadRequestException("400 - Algorithm was invalid or not given! "
                                          f"Please, choose one of these options: "
                                          f"{supported_grouping_algorithms}.")

            elif "k_means" in algorithm:
                num_clusters = event.get("num_clusters", 8)
                init_method = event.get("init_method", "k-means++")
                num_init = event.get("num_init", 10)
                max_iter = event.get("max_iter", 300)
                tolerance = event.get("tolerance", 1e-4)
                seed = event.get("seed", None)

                print(f" - Number of clusters: {num_clusters}")
                print(f" - Initialization method: {init_method}")
                print(f" - Initialization number: {num_init}")
                print(f" - Maximum of iterations: {max_iter}")
                print(f" - Tolerance: {tolerance}")
                print(f" - Seed: {seed}")

                print("\nRunning K-Means algorithm...")
                k_means.run(dataset_url, delimiter, num_clusters, init_method, num_init, max_iter, tolerance, seed)
                print("K-Means algorithm was completed successful!\n")

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
