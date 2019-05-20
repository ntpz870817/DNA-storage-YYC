"""
Name: Abstract method

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) DNA encoding.
             (2) DNA decoding.

Advantages: (1) high compressibility, maximum compressibility to 1/2 of the original data.
            (2) preventing repetitive motifs, like ATCGATCG...
            (3) increase the number of sequence changes (far exceed YYC, 5,566,277,615,616 cases), increasing data security.
"""

import abc


# noinspection PyPep8Naming,PyMethodMayBeStatic
class abs_method(metaclass=abc.ABCMeta):

    def encode(self, matrix, file_size):
        raise Exception("Subclass must override this method")

    def decode(self, dna_motifs):
        raise Exception("Subclass must override this method")
