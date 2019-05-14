"""
Name: Error Correcting

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Add error correcting.
             (2) Remove error correcting.
             (3) Check the matrix correcting.
             (4) Repair the wrong matrix.

"""

import verify.hamming as hamming


def add_code(method_name="hamming", matrix=None):

    new_matrix = []

    if method_name == "hamming":
        for row in range(len(matrix)):
            new_matrix.append(hamming.add_code(matrix[row]))

    return new_matrix


def remove_code(method_name="hamming", matrix=None):

    new_matrix = []

    if method_name == "hamming":
        for row in range(len(matrix)):
            new_matrix.append(hamming.remove_code(matrix[row]))

    return new_matrix


def check(method_name="hamming", matrix=None):
    check_result = []

    if method_name == "hamming":
        for row in range(len(matrix)):
            check_result.append(hamming.check(matrix[row]))

    return check_result


def repair(method_name="hamming", matrix=None):

    new_matrix = []

    if method_name == "hamming":
        for row in range(len(matrix)):
            new_matrix.append(hamming.repair(matrix[row]))

    return new_matrix
