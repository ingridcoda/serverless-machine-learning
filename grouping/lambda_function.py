import json

import k_means
from exceptions import *


def handler(event, context):
    supported_algorithms = ['k_means']

    try:
        algorithm = event.get("algorithm", None)
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

        print("Parameters values:\n")
        print(f" - Algorithm type: {algorithm}")
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

        if not event or not algorithm:
            raise BadRequestException("400 - Parameter 'algorithm' is required.")

        elif algorithm not in supported_algorithms:
            raise BadRequestException("400 - Algorithm type was invalid or not given! "
                                      f"Please, choose one of these options: {supported_algorithms}.")

        elif "k_means" in algorithm:
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
