"""
Name: Rules finder

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Find the best rule that work best for binary file.
"""


import utils.model_saver as model_saver
from utils import monitor


def find_best_rule(file_binaries, rules_path="rules.pkl", model_path="models.pkl"):
    """
    introduction: Find best rule based on tendency of file data.

    :param file_binaries: Binaries from file.

    :param rules_path: Path of rule object set (using pickle to save).

    :param model_path: Path of classifiers (using pickle to save).

    :return: Objects of the best rule.
    """

    if len(file_binaries[0]) % 9 != 0:
        print("wrong")
        return

    data_indexes = []
    for row in range(0, len(file_binaries), 2):
        for col in range(0, len(file_binaries[row]), 9):
            if row + 1 < len(file_binaries) and col + 9 < len(file_binaries[row]):
                data_indexes.append([int("".join(list(map(str, file_binaries[row][col: col + 9] +
                                                          file_binaries[row + 1][col: col + 9]))), 2)])

    # noinspection PyUnusedLocal
    rules_weight = [0 for index in range(6144)]

    classifiers = model_saver.load_model(model_path)

    m = monitor.Monitor()
    for classifier_index in range(len(classifiers)):
        m.output(classifier_index, len(classifiers))
        rules_weight[classifier_index] += sum(classifiers[classifier_index].predict(data_indexes))

    rules = model_saver.load_model(rules_path)

    best_rules = []
    for index in range(len(rules_weight)):
        if rules_weight[index] == max(rules_weight):
            best_rules.append(rules[index])

    return best_rules
