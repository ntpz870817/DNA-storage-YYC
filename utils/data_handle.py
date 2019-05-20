"""
Name: Data Handle

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): Conversion of DNA motifs and binary document
"""

import os
import tkinter as tk
from tkinter import filedialog
import numpy
import struct
import math
import sys

import utils.log as log
import utils.monitor as monitor


# noinspection PyUnresolvedReferences,PyBroadException,PyProtectedMember
def read_binary_from_all(interval=120):
    """
    introduction: Writing DNA motif set from documents.

    :param interval: The cut length of DNA motif.
                      Considering current DNA synthesis factors, we usually set 120 bases as a motif.

    :return matrix: A corresponding DNA motif string in which each row acts as a motif.
                    Type: two-dimensional list(int)

    :return size: This refers to file size, to reduce redundant bits when transferring DNA to binary files.
                  Type: int
    """

    m = monitor.Monitor()
    try:
        # Search file path by GUI to read
        tkinter = tk.Tk()
        tkinter.withdraw()
        path = filedialog.askopenfilename()

        # Open selected file
        with open(path, mode='rb') as file:

            log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                       "Read binary matrix from file: " + path)

            size = os.path.getsize(path)

            # Set init storage matrix
            matrix = numpy.zeros((math.ceil(size * 8 / interval), interval))

            row = 0
            col = 0
            for byte_index in range(size):
                m.print(byte_index, size)
                # Read a file as bytes
                one_byte = file.read(1)
                element = int(struct.unpack("B", one_byte)[0])
                bit_matrix = numpy.zeros(8, dtype=bool)

                # Change byte to bit
                for bit_index in range(8):
                    bit_matrix[bit_index] = element % 2
                    element = int(element / 2)

                for bit_index in range(8):
                    matrix[row][col] = bit_matrix[7 - bit_index]
                    col += 1
                    if col >= interval:
                        col = 0
                        row += 1

        return matrix.tolist(), size
    except Exception:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please complete the operation again!")


# noinspection PyBroadException,PyProtectedMember
def write_all_from_binary(matrix, size):
    """
    introduction: Writing binary matrix to document.

    :param matrix: A corresponding DNA motif string in which each row acts as a motif.
                    Type: two-dimensional list(int)

    :param size: This refers to file size, to reduce redundant bits when transferring DNA to binary files.
                  Type: int

    """
    m = monitor.Monitor()

    try:

        # search file path by GUI to save
        tkinter = tk.Tk()
        tkinter.withdraw()
        path = filedialog.asksaveasfilename()

        with open(path, 'wb+') as file:
            log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                       "Write file from binary matrix: " + path)

            # Change bit to byte (8 -> 1), and write a file as bytes
            bit_index = 0
            temp_byte = 0
            for row in range(len(matrix)):
                m.print(row, len(matrix))
                for col in range(len(matrix[0])):
                    bit_index += 1
                    temp_byte *= 2
                    temp_byte += matrix[row][col]
                    if bit_index == 8:
                        if size >= 0:
                            file.write(struct.pack("B", int(temp_byte)))
                            size -= 1
                        bit_index = 0
                        temp_byte = 0
    except Exception:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please complete the operation again!")


# noinspection PyBroadException,PyProtectedMember
def read_dna_file():
    """
    introduction: Reading DNA motif set from documents.

    :return dna_motifs: A corresponding DNA sequence string in which each row acts as a sequence.
                         Type: one-dimensional list(string)
    """

    m = monitor.Monitor()

    dna_motifs = []

    try:
        # Search file path by GUI to save
        tkinter = tk.Tk()
        tkinter.withdraw()
        path = filedialog.askopenfilename()

        with open(path, 'r') as file:
            log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                       "Read DNA motifs from file: " + path)

            # Read current file by line
            lines = file.readlines()
            for index in range(len(lines)):
                m.print(index, len(lines))
                line = lines[index]
                dna_motifs.append([line[col] for col in range(len(line) - 1)])

        return dna_motifs
    except Exception:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please complete the operation again!")


# noinspection PyProtectedMember,PyBroadException
def write_dna_file(dna_motifs):
    """
    introduction: Writing DNA motif set to documents.

    :param dna_motifs: A corresponding DNA sequence string in which each row acts as a sequence.
                        Type: one-dimensional list(string)
    """

    m = monitor.Monitor()

    try:
        tkinter = tk.Tk()
        tkinter.withdraw()
        path = filedialog.asksaveasfilename()
        with open(path, 'w') as file:
            log.output(log.NORMAL, str(__name__), str(sys._getframe().f_code.co_name),
                       "Write DNA motifs to file: " + path)
            for row in range(len(dna_motifs)):
                m.print(row, len(dna_motifs))
                file.write("".join(dna_motifs[row]) + "\n")
        return dna_motifs
    except Exception:
        log.output(log.ERROR, str(__name__), str(sys._getframe().f_code.co_name),
                   "The file selection operation was not performed correctly. Please complete the operation again!")
