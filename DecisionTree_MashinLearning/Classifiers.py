from DataExtractor import DataExtractor

import sklearn
from sklearn import tree, neighbors, linear_model
from sklearn.ensemble import BaggingClassifier, VotingClassifier
from sklearn.feature_selection import mutual_info_classif
import matplotlib.pyplot as plt
import numpy as np


class Classifiers:
    def __init__(self, filepath):
        self.x_train, self.x_test, self.y_train, self.y_test = DataExtractor(filepath).split_validation()

    def information_gain(self):
        res = dict(zip(self.x_train.columns.values, mutual_info_classif(self.x_train, self.y_train)))
        print(res)
        objects = self.x_train.columns.values
        y_pos = np.arange(len(objects))
        performance = mutual_info_classif(self.x_train, self.y_train)

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Information Gain')
        plt.title('Programming language usage')
        plt.show()

    def decision_tree(self, max_depth):
        accuracy_history_train = []
        accuracy_history_test = []
        # for i in range(max_depth+1):
        # print("Epoch number: ", i)
        classifier = tree.DecisionTreeClassifier(max_depth=max_depth, )
        classifier.fit(self.x_train, self.y_train)

        y_predict_train = classifier.predict(self.x_train)
        y_predict = classifier.predict(self.x_test)
        print("Decision Tree")
        print("For Train Predicts\n", sklearn.metrics.classification_report(self.y_train, y_predict_train))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        print("For Test Predicts\n", sklearn.metrics.classification_report(self.y_test, y_predict))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_test, y_predict))
        print("\n")

        # export the decision tree to a tree.dot file 
        # for visualizing the plot easily anywhere 
        import pydotplus
        dot_data = export_graphviz(classifier, out_file=None, feature_names=['Production Cost'])
        '
        # using the graph_from_dot_data to visualize the tree formed by the regressor
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf("tree.pdf")

        #     accuracy_history_test.append(sklearn.metrics.accuracy_score(self.y_test, y_predict))
        #     accuracy_history_train.append(sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        # self.plot_accuracy(accuracy_history_train, accuracy_history_test)

    def k_nearest_neighbors(self, k):
        accuracy_history_train = []
        accuracy_history_test = []
        # for i in range(k):
        # print("Epoch number: ", i)
        neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
        neigh.fit(self.x_train, self.y_train)

        y_predict_train = neigh.predict(self.x_train)
        y_predict = neigh.predict(self.x_test)

        print("K Nearest Neighbor")
        print("For Train Predicts\n", sklearn.metrics.classification_report(self.y_train, y_predict_train))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        print("For Test Predicts\n", sklearn.metrics.classification_report(self.y_test, y_predict))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_test, y_predict))
        print("\n")

        accuracy_history_test.append(sklearn.metrics.accuracy_score(self.y_test, y_predict))
        accuracy_history_train.append(sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        # self.plot_accuracy(accuracy_history_train, accuracy_history_test)

    def logistic_classifier(self):
        logistic = linear_model.LogisticRegression()
        logistic.fit(self.x_train, self.y_train)

        y_predict_train = logistic.predict(self.x_train)
        y_predict = logistic.predict(self.x_test)

        print("Logistic Classifier")
        print("For Train Predicts\n", sklearn.metrics.classification_report(self.y_train, y_predict_train))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        print("For Test Predicts\n", sklearn.metrics.classification_report(self.y_test, y_predict))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_test, y_predict))
        print("\n")

    @staticmethod
    def plot_accuracy(accuracy_train, accuracy_test):
        plt.plot(accuracy_test)
        plt.plot(accuracy_train)
        plt.legend(["Test", "Train"])
        plt.show()

    def bagging(self, estimator, number_of_estimator):
        bag = BaggingClassifier(base_estimator=estimator, n_estimators=number_of_estimator, max_features=0.5)
        bag.fit(self.x_train, self.y_train)

        y_predict_train = bag.predict(self.x_train)
        y_predict = bag.predict(self.x_test)

        print("For Train Predicts\n", sklearn.metrics.classification_report(self.y_train, y_predict_train))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        print("For Test Predicts\n", sklearn.metrics.classification_report(self.y_test, y_predict))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_test, y_predict))

    def voting(self, estimators):
        vote = VotingClassifier(estimators=estimators)
        vote.fit(self.x_train, self.y_train)

        y_predict_train = vote.predict(self.x_train)
        y_predict = vote.predict(self.x_test)

        print("For Train Predicts\n", sklearn.metrics.classification_report(self.y_train, y_predict_train))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_train, y_predict_train))
        print("For Test Predicts\n", sklearn.metrics.classification_report(self.y_test, y_predict))
        print("Accuracy: ", sklearn.metrics.accuracy_score(self.y_test, y_predict))

