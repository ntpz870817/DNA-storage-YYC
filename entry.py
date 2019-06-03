"""
Name: Entry function

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): (1) Get the binary file, encode the binary file by YYC, and output the dna motifs file.
             (2) Get the dna motifs file, decode the dna motifs by YYC, and output the binary file.
"""

import utils.model_saver as saver
import utils.data_handle as data_handle


def encode(method, file_path, dna_path, model_path, interval=None):
    """
    introduction: Get the binary file, encode the binary file by YYC, and output the dna motifs file.

    :param method: method named yyc (Initialized method).
                    Type: YYC.

    :param file_path: Binary file path that need to be encoded.
                       Type: String.

    :param dna_path: The saved DNA motifs file path.
                      Type: String.

    :param model_path: The path to save the method as a file.
                        Type: String

    :param interval: The cut length of DNA motif.
                      Considering current DNA synthesis factors, we usually set 120 bases as a motif.
                      Type: Int.
    """
    input_matrix, size = data_handle.read_binary_from_all(path=file_path, interval=interval)
    dna_motifs = method.encode(input_matrix, size)
    data_handle.write_dna_file(dna_path, dna_motifs)
    saver.save_model(model_path, method)


def decode(model_path, dna_path, file_path):
    """
    introduction: Get the dna motifs file, decode the dna motifs by YYC, and output the binary file.

    :param model_path: The path to save the method as a file.
                        Type: String

    :param dna_path: The saved DNA motifs file path.
                      Type: String.

    :param file_path: Binary file path that need to output.
                       Type: String.
    """
    method = saver.load_model(model_path)
    dna_motifs = data_handle.read_dna_file(dna_path)
    output_matrix = method.decode(dna_motifs)
    data_handle.write_all_from_binary(file_path, output_matrix, method.file_size)
