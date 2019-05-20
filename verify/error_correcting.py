"""
Name: Error Correcting

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Add error correcting.
             (2) Remove error correcting.
             (3) Check the matrix correcting.
             (4) Repair the wrong matrix.

"""

import abc


# noinspection PyMethodMayBeStatic,PyPep8Naming
class error_correcting(metaclass=abc.ABCMeta):

    def add(self, matrix):
        raise Exception("Subclass must override this method")

    def remove(self, matrix):
        raise Exception("Subclass must override this method")

    def check(self, matrix):
        raise Exception("Subclass must override this method")

    def repair(self, matrix):
        raise Exception("Subclass must override this method")
