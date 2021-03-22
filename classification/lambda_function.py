import json

import decision_tree
from exceptions import *


def handler(event, context):
    try:
        if not event or not event["algorithm"]:
            raise BadRequestException("400 - Parâmetro 'algorithm' requerido.")

        elif "decision_tree" in event["algorithm"]:
            print("Executando algoritmo de árvore de decisão...")
            decision_tree.run_decision_tree()
            print("Algoritmo de árvore de decisão executado com sucesso!")

            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "Message": "Executado com sucesso!"
                })
            }
        elif "knn" in event["algorithm"]:
            raise BadRequestException("400 - Algoritmo não implementado.")

        elif "naive_bayes" in event:
            raise BadRequestException("400 - Algoritmo não implementado.")

        elif "svm" in event["algorithm"]:
            raise BadRequestException("400 - Algoritmo não implementado.")

        elif "logistic_regression" in event["algorithm"]:
            raise BadRequestException("400 - Algoritmo não implementado.")

        else:
            raise BadRequestException("400 - Tipo de algoritmo não informado ou inválido! "
                                      "Por favor, escolha dentre as seguintes opções: "
                                      "['decision_tree', 'knn', 'naive_bayes', 'svm', 'logistic_regression'].")

    except BadRequestException as e:
        raise e

    except Exception as e:
        raise UnknownException("500 - Erro inesperado.", e)


if __name__ == "__main__":
    handler('', '')
