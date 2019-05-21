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
class e_d(metaclass=abc.ABCMeta):

    def __init__(self):
        # Conversing base to actual index, where index 0 <-> A, index 1 <-> T, index 2 <-> C, index 3 <-> G.
        self.base_index = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        self.index_base = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}

    def encode(self, matrix, file_size):
        raise Exception("Subclass must override this method")

    def decode(self, dna_motifs):
        raise Exception("Subclass must override this method")
