from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score


def load_dataset():
    iris = load_iris()
    return iris.data, iris.target


def decision_tree_by_entropy_criteria(data, target):
    classifier = tree.DecisionTreeClassifier(criterion="entropy")
    trained = classifier.fit(data, target)
    return trained, classifier


def decision_tree_by_gini_criteria(data, target):
    classifier = tree.DecisionTreeClassifier(criterion="gini")
    trained = classifier.fit(data, target)
    return trained, classifier


def run_decision_tree():
    try:
        data, target = load_dataset()

        print("Executando árvore de decisão por entropia:")
        trained, classifier = decision_tree_by_entropy_criteria(data, target)
        print("Predições:", trained.predict([[2., 2., 2., 2.]]))

        allScores = cross_val_score(classifier, data, target, cv=10)
        print("Scores:")
        print(allScores)
        print(f"Acurácia: {allScores.mean() * 100}%\n\n")

        print("Executando árvore de decisão por indice gini:")
        trained, classifier = decision_tree_by_gini_criteria(data, target)
        print("Predições:", trained.predict([[2., 2., 2., 2.]]))

        allScores = cross_val_score(classifier, data, target, cv=10)
        print("Scores:")
        print(allScores)
        print(f"Acurácia: {allScores.mean() * 100}%")

    except Exception as e:
        raise e
