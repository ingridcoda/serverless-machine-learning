import json

import decision_tree
from exceptions import *


def handler(event, context):
    try:
        algorithm = event.get("algorithm", None)
        kfold = event.get("kfold", None)
        seed = event.get("seed", None)
        test_size = event.get("test_size", None)
        dataset_name = event.get("dataset_name", None)
        dataset_url = event.get("dataset_url", None)

        if not event or not algorithm:
            raise BadRequestException("400 - Parameter 'algorithm' is required.")

        elif "decision_tree" in algorithm:
            print("Running decision tree algorithm...")
            decision_tree.run_decision_tree(kfold, seed, test_size, dataset_name, dataset_url)
            print("Decision tree algorithm was completed successful!")

            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "Message": "Success!"
                })
            }

        elif "knn" in algorithm:
            raise BadRequestException("400 - Algorithm not implemented.")

        elif "naive_bayes" in algorithm:
            raise BadRequestException("400 - Algorithm not implemented.")

        elif "svm" in algorithm:
            raise BadRequestException("400 - Algorithm not implemented.")

        elif "logistic_regression" in algorithm:
            raise BadRequestException("400 - Algorithm not implemented.")

        else:
            raise BadRequestException("400 - Algorithm type was invalid or not given! "
                                      "Please, choose one of these options: "
                                      "['decision_tree', 'knn', 'naive_bayes', 'svm', 'logistic_regression'].")

    except BadRequestException as e:
        raise e

    except Exception as e:
        raise UnknownException("500 - Unexpected error.", e)


if __name__ == "__main__":
    handler({}, '')
