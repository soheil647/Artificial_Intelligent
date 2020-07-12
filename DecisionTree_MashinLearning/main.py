from DataExtractor import DataExtractor
from Classifiers import Classifiers
from sklearn import tree, neighbors, linear_model


# DE = DataExtractor("./data.csv")
# print(DE.split_labels())
classifiers = Classifiers('./data.csv')
# classifiers.information_gain()

# classifiers.decision_tree(20)
# classifiers.k_nearest_neighbors(50)
# classifiers.logistic_classifier()

# classifiers.bagging(tree.DecisionTreeClassifier(max_depth=20), 10)

classifiers.bagging(neighbors.KNeighborsClassifier(n_neighbors=2), 10)

# classifiers.random_forest(4, 100, False)

classifiers.voting([('dt', tree.DecisionTreeClassifier(max_depth=4)), ('knn', neighbors.KNeighborsClassifier(n_neighbors=40)), ('lr', linear_model.LogisticRegression())])
