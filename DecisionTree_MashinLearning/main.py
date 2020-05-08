from DataExtractor import DataExtractor
from Classifiers import Classifiers
from sklearn import tree, neighbors, linear_model


# DE = DataExtractor("./data.csv")
# print(DE.split_labels())
classifiers = Classifiers('./data.csv')
classifiers.information_gain()

classifiers.decision_tree(50)
# classifiers.k_nearest_neighbors(18)
# classifiers.logistic_classifier()

classifiers.bagging(tree.DecisionTreeClassifier(max_depth=4), 10)
# classifiers.bagging(neighbors.KNeighborsClassifier(n_neighbors=18), 20)

# classifiers.voting([('dt', tree.DecisionTreeClassifier(max_depth=5)), ('knn', neighbors.KNeighborsClassifier(n_neighbors=18)), ('lr', linear_model.LogisticRegression())])
