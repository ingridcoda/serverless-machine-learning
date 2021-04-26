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

        print("Parameters values:\n")
        print(f" - Type: {_type}")
        print(f" - Algorithm: {algorithm}")

        if not event or not _type:
            raise BadRequestException("400 - Parameter 'type' is required.")

        elif _type not in supported_types:
            raise BadRequestException("400 - Type was invalid or not given! "
                                      f"Please, choose one of these options: {supported_types}.")

        elif not event or not algorithm:
            raise BadRequestException("400 - Parameter 'algorithm' is required.")

        elif _type == "classification":
            kfold = event.get("kfold", 10)
            seed = event.get("seed", 7)
            test_size = event.get("test_size", 0.25)
            dataset_name = event.get("dataset_name", "iris")
            dataset_url = event.get("dataset_url", None)
            print(f" - Dataset: {dataset_url if dataset_url else dataset_name}")
            print(f" - Number of folds: {kfold}")
            print(f" - Seed: {seed}")
            print(f" - Test size: {test_size}")

            if algorithm not in supported_classification_algorithms:
                raise BadRequestException("400 - Algorithm was invalid or not given! "
                                          f"Please, choose one of these options: "
                                          f"{supported_classification_algorithms}.")

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
                num_samples = event.get("num_samples", 100)
                num_features = event.get("num_features", 2)
                centers = event.get("centers", None)
                cluster_std = event.get("cluster_std", 1.0)
                shuffle = event.get("shuffle", True)
                print(f" - Number of clusters: {num_clusters}")
                print(f" - Initialization method: {init_method}")
                print(f" - Initialization number: {num_init}")
                print(f" - Maximum of iterations: {max_iter}")
                print(f" - Tolerance: {tolerance}")
                print(f" - Seed: {seed}")
                print(f" - Number of samples of generated dataset: {num_samples}")
                print(f" - Number of features of generated dataset: {num_features}")
                print(f" - Number of centers of generated dataset: {centers}")
                print(f" - Standard deviation of generated dataset: {cluster_std}")
                print(f" - Shuffle generated dataset: {shuffle}")
                print("\nRunning K-Means algorithm...")
                k_means.run(num_clusters, init_method, num_init, max_iter, tolerance, seed,
                            num_samples, num_features, centers, cluster_std, shuffle)
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
