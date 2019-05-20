"""
Name: Hamming Error Correcting

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Add error correcting.
             (2) Remove error correcting.
             (3) Check the matrix correcting.
             (4) Repair the wrong matrix.

"""

import math
import sys
from utils import log
import verify.error_correcting as error_correcting


# noinspection PyMethodMayBeStatic
class Hamming(error_correcting.error_correcting):

    # noinspection PyProtectedMember
    def add(self, binary_list):

        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Add hamming code to a line list.")

        new_binary_list = []
        total_length = len(binary_list) + self.get_hamming_length(len(binary_list))

        # init hamming list
        verify_position = 0
        verified_position = 0
        for index in range(total_length):
            if int(math.pow(2, verify_position)) == index:
                new_binary_list[index] = 0
                verify_position += 1
            else:
                new_binary_list.append(binary_list[verified_position])
                verified_position += 1

        # set verification code
        verify_position = 0
        for index in range(total_length):
            calculated_count = index + 1
            if int(math.pow(2, verify_position)) == index:
                calculated_position = verify_position
                while calculated_position < total_length:
                    new_binary_list[index] = self.xor(new_binary_list[index], new_binary_list[calculated_position])
                    calculated_count -= 1
                    calculated_position += 1
                    if calculated_count == 0:
                        calculated_count = index + 1
                        calculated_position += index + 1
                verify_position += 1

        return new_binary_list

    # noinspection PyProtectedMember
    def remove(self, binary_list):

        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Remove hamming code to a line list.")

        new_binary_list = []
        index = 0

        for position in range(len(binary_list)):
            if position == int(math.pow(2, index)):
                index += 1
            else:
                new_binary_list.append(binary_list[position])

        return new_binary_list

    # noinspection PyProtectedMember
    def check(self, binary_list):

        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Check hamming code to a line list.")

        verify_position = 0
        for index in range(len(binary_list)):
            result = 0
            calculated_count = index + 1
            if int(math.pow(2, verify_position)) == index:
                calculated_position = verify_position
                while calculated_position < len(binary_list):
                    result = self.xor(result, binary_list[calculated_position])
                    calculated_count -= 1
                    calculated_position += 1
                    if calculated_count == 0:
                        calculated_count = index + 1
                        calculated_position += index + 1
                verify_position += 1
            if result != 0:
                return False

        return True

    # noinspection PyProtectedMember
    def repair(self, binary_list):

        log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                   "Repair hamming code to a line list.")

        # TODO finish the repair operation in hamming code

        return binary_list

    def get_hamming_length(self, matrix_length):

        hamming_length = 2

        while math.pow(2, hamming_length) - 1 < matrix_length + hamming_length:
            hamming_length += 1

        return hamming_length

    def xor(self, number1, number2):
        return 0 if number1 == number2 else 1
