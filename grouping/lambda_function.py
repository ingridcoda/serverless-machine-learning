from exceptions import *


def handler(event, context):
    try:
        if not event or not event["algorithm"]:
            raise BadRequestException("400 - Parâmetro 'algorithm' requerido.")

        elif "k_means" in event["algorithm"]:
            raise BadRequestException("400 - Algoritmo não implementado.")

        else:
            raise BadRequestException("400 - Tipo de algoritmo não informado ou inválido! "
                                      "Por favor, escolha dentre as seguintes opções: "
                                      "['k_means'].")

    except BadRequestException as e:
        raise e

    except Exception as e:
        raise UnknownException("500 - Erro inesperado.", e)


if __name__ == "__main__":
    handler('', '')
