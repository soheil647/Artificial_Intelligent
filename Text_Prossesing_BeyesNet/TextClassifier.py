import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
import itertools


class TextClassifier:
    def __init__(self):
        self.num_texes = {}
        self.log_class_priors = {}
        self.word_counts = {}
        self.vocab = set()
        self.classes = ['BUSINESS', 'TRAVEL', 'STYLE & BEAUTY']
        # self.classes = ['BUSINESS', 'TRAVEL']
        self.correct_detected_category = {}

    @staticmethod
    def __get_word_counts(tokenized_text):
        word_counts = {}
        for word in tokenized_text:
            word_counts[word] = word_counts.get(word, 0.0) + 1.0
        return word_counts

    def split_validation_data(self, data, target):
        train_data = [[]]
        train_target = [[]]
        class_train_data = [[]]
        class_train_target = [[]]
        class_validation_data = [[]]
        class_validation_target = [[]]
        for i in range(len(self.classes)):
            train_data.append([])
            train_target.append([])
            class_train_data.append([])
            class_train_target.append([])
            class_validation_data.append([])
            class_validation_target.append([])
        for x, y in zip(data, target):
            for i in range(len(self.classes)):
                if y == self.classes[i]:
                    train_data[i].append(x)
                    train_target[i].append(y)

        for i in range(len(self.classes)):
            class_train_data[i], class_validation_data[i], class_train_target[i], class_validation_target[
                i] = train_test_split(train_data[i], train_target[i], test_size=0.2)

        (class_train_data, class_train_target), (
            class_validation_data, class_validation_target) = self.over_sample_data(class_train_data,
                                                                                    class_validation_data,
                                                                                    class_train_target,
                                                                                    class_validation_target)

        val_data = []
        train_data = []
        train_target = []
        val_target = []
        for i in range(len(self.classes)):
            train_data += class_train_data[i]
            train_target += class_train_target[i]
            val_data += class_validation_data[i]
            val_target += class_validation_target[i]

        train_data_frame = pd.DataFrame(train_data)[0]
        train_target_frame = pd.DataFrame(train_target)[0]

        validation_data_frame = pd.DataFrame(val_data)[0]
        validation_target_frame = pd.DataFrame(val_target)[0]
        return (train_data_frame, train_target_frame), (validation_data_frame, validation_target_frame)

    def over_sample_data(self, class_train_data, class_validation_data, class_train_target, class_validation_target):
        for i in range(len(self.classes)):
            repeat_element = len(max(class_train_data, key=len)) - len(class_train_data[i])
            class_train_data[i].extend(random.sample(class_train_data[0], repeat_element))

            repeat_element = len(max(class_train_target, key=len)) - len(class_train_target[i])
            class_train_target[i].extend(random.sample(class_train_target[0], repeat_element))

            repeat_element = len(max(class_validation_data, key=len)) - len(class_validation_data[i])
            class_validation_data[i].extend(random.sample(class_validation_data[0], repeat_element))

            repeat_element = len(max(class_validation_target, key=len)) - len(class_validation_target[i])
            class_validation_target[i].extend(random.sample(class_validation_target[0], repeat_element))

        return (class_train_data, class_train_target), (class_validation_data, class_validation_target)

    def fit(self, data, target):
        total_number_of_text = len(data)
        for class_type in self.classes:
            self.num_texes[class_type] = sum(1 for label in target if label == class_type)
            self.log_class_priors[class_type] = math.log(self.num_texes[class_type] / total_number_of_text)
            self.word_counts[class_type] = {}

        for x, y in zip(data, target):
            if not self.classes.__contains__(y):
                continue
            class_type = y
            counts = self.__get_word_counts(x)
            for word, count in counts.items():
                if word not in self.vocab:
                    self.vocab.add(word)
                if word not in self.word_counts[class_type]:
                    self.word_counts[class_type][word] = 0.0
                self.word_counts[class_type][word] += count

    def evaluate(self, validation_data, validation_target):
        result = self.predict(validation_data)
        all_category = dict.fromkeys(self.classes, 0)
        detected_category = dict.fromkeys(self.classes, 0)
        correct_detected_category = dict.fromkeys(self.classes, 0)
        total = len(result)
        for i in range(len(validation_target)):
            for class_type in self.classes:
                if class_type == validation_target[i] and validation_target[i] == result[i]:
                    correct_detected_category[class_type] += 1
                if class_type == validation_target[i]:
                    all_category[class_type] += 1
                if class_type == result[i]:
                    detected_category[class_type] += 1

        recall = dict.fromkeys(self.classes, 0.0)
        precision = dict.fromkeys(self.classes, 0.0)

        for class_type in self.classes:
            recall[class_type] = correct_detected_category[class_type] / all_category[class_type]
            precision[class_type] = correct_detected_category[class_type] / detected_category[class_type]
        accuracy = sum(correct_detected_category.values()) / total
        print('Recall is: ', recall)
        print('Precision is: ', precision)
        print('Accuracy is: ', accuracy)

    def predict(self, tokenized_test):
        result = []
        for x in tokenized_test:
            counts = self.__get_word_counts(x)
            class_type_score = dict.fromkeys(self.classes, 0.0)
            for word, _ in counts.items():
                if word not in self.vocab:
                    continue

                for class_type in self.classes:
                    log_w_given_class = math.log((self.word_counts[class_type].get(word, 0.0) + 1) / (
                            self.num_texes[class_type] + len(self.vocab)))
                    class_type_score[class_type] += log_w_given_class

            for class_type in self.classes:
                class_type_score[class_type] += self.log_class_priors[class_type]

            class_type_score = {k: v for k, v in sorted(class_type_score.items(), key=lambda item: item[1])}
            result.append(list(class_type_score.keys())[-1])
        return result

    def plot_confusion_matrix(self,
                              cm,
                              target_names=['1', '2', '3', '4'],
                              title='Confusion matrix',
                              cmap=None,
                              normalize=False):

        accuracy = np.trace(cm) / float(np.sum(cm))
        misclass = 1 - accuracy

        if cmap is None:
            cmap = plt.get_cmap('Blues')

        plt.figure()
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()

        if target_names is not None:
            tick_marks = np.arange(len(target_names))
            plt.xticks(tick_marks, target_names, rotation=0)
            plt.yticks(tick_marks, target_names)

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        thresh = cm.max() / 1.5 if normalize else cm.max() / 2
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            if normalize:
                plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
        plt.show()

    def confusion(self, train_target, train_data):
        train_prediction = self.predict(train_data)
        cm = confusion_matrix(y_true=train_target, y_pred=train_prediction)

        names = []
        for i in range(43):
            names.append(i)
        self.plot_confusion_matrix(cm=cm,
                                   normalize=False,
                                   target_names=self.classes,
                                   title="Confusion Matrix")
