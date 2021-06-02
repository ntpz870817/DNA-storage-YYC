"""
Name: Inherent property

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Common attributes in constraint methods.

"""
import itertools
import sys

import numpy
import yyc.utils.log as log
from yyc.utils.monitor import Monitor


#    1: ["A", [0, 0, 1, 1], [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]]
#  496: ["A", [0, 1, 0, 1], [[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]]]
#  888: ["A", [1, 0, 0, 1], [[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]]]
# 1536: ["A", [1, 1, 0, 0], [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]]]


def get_yyc_rules(need_log=False):
    rules = []
    temp_rule1 = ["".join(x) for x in itertools.product("01", repeat=4)]
    temp_rule2 = ["".join(x) for x in itertools.product("01", repeat=16)]

    m = Monitor()

    if need_log:
        # noinspection PyProtectedMember
        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Find all the available Yin-Yang rules.")

    count, step = 0, 0
    for base in ["A", "T", "C", "G"]:
        for rule1index in range(len(temp_rule1)):
            for rule2index in range(len(temp_rule2)):
                rule1 = list(map(int, list(temp_rule1[rule1index])))
                rule2 = numpy.array(list(map(int, list(temp_rule2[rule2index])))).reshape(4, 4).tolist()
                if _check(rule1, rule2):
                    rules.append(YYCRule(rule1, rule2, base, count))
                    count += 1

                step += 1

                if need_log:
                    m.output(step, len(temp_rule1) * len(temp_rule2) * 4)

    return rules


# noinspection PyProtectedMember
def get_yyc_rule_by_index(index, need_log=False):
    """
    introduction: Get Yin and Yang rule of YYC by index (1536 types of rules)

    :param index: rule index.

    :param need_log: Show the log.

    :return: YYC rule with [self.support_base, self.rule1, self.rule2].
    """
    rules = get_yyc_rules(need_log)

    if index < 0 or index >= len(rules):
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "We have " + str(len(rules)) + " rules, index " + str(index) + " is wrong!")

    if need_log:
        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Current Rule is " + str(rules[index].get_info()) + ".")

    return rules[index].get_info()


def _check(rule1, rule2):
    """
    introduction: Verify the correctness of the YYC rules.

    :param rule1: Correspondence between base and binary data (RULE 1).
    :param rule2: Conversion rule between base and binary data based on support base and current base (RULE 2).

    :return: Check result.
    """

    for index in range(len(rule1)):
        if rule1[index] != 0 and rule1[index] != 1:
            return False

    if sum(rule1) != 2:
        return False

    if rule1[0] == rule1[1]:
        same = [0, 1, 2, 3]
    elif rule1[0] == rule1[2]:
        same = [0, 2, 1, 3]
    else:
        same = [0, 3, 1, 2]

    for row in range(len(rule2)):
        if rule2[row][same[0]] + rule2[row][same[1]] != 1 or rule2[row][same[0]] * rule2[row][same[1]] != 0:
            return False
        if rule2[row][same[2]] + rule2[row][same[3]] != 1 or rule2[row][same[2]] * rule2[row][same[3]] != 0:
            return False

    return True


class YYCRule:

    def __init__(self, rule1, rule2, support_base, identity):
        self.b2i = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        self.i2b = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        self.rule1 = rule1
        self.rule2 = rule2
        self.support_base = support_base
        self.identity = identity

    def lists_to_motif(self, upper_list, lower_list):
        motif = []

        for col in range(len(upper_list)):
            if col > 0:
                motif.append(self.__binary_to_base__(upper_list[col], lower_list[col], motif[col - 1]))
            else:
                motif.append(self.__binary_to_base__(upper_list[col], lower_list[col], self.support_base))
        return motif

    def __str__(self):
        return "[" + self.support_base + ", " + str(self.rule1) + ", " + str(self.rule2) + "]"

    def __binary_to_base__(self, upper_bit, lower_bit, support_base):

        current_options = []
        for index in range(len(self.rule1)):
            if self.rule1[index] == int(upper_bit):
                current_options.append(index)

        if self.rule2[self.b2i.get(support_base)][current_options[0]] == int(lower_bit):
            one_base = self.i2b[current_options[0]]
        else:
            one_base = self.i2b[current_options[1]]

        return one_base

    def get_info(self):
        return {"v": self.support_base, "yang": self.rule1, "yin": self.rule2}
