"""
Name: Validity

Coder: HaoLing ZHANG (BGI-Research)[V1]

Function(s):
Check the validity of requested DNA sequence.
The validity describes the friendly index for DNA synthesis, sequencing and related operations
"""

import re
import subprocess
import math


def check(sequence, max_homopolymer=math.inf, max_content=1, min_free_energy=None):
    """
    Check the validity of requested DNA sequence.

    :param sequence: requested DNA sequence.
    :param max_homopolymer: maximum length of homopolymer.
    :param max_content: maximum content of C and G, which means GC content is in [1 - max_content, max_content].
    :param min_free_energy: the free energy of DNA sequence is lower than required min free energy.

    :return: whether the DNA sequence can be considered as valid for DNA synthesis and sequencing.
    """
    if not homopolymer(sequence, max_homopolymer):
        return False
    if not cg_content(sequence, max_content):
        return False
    if not fold(sequence, min_free_energy):
        return False

    return True


def homopolymer(sequence, max_homopolymer):
    """
    Check the max homopolymer of requested DNA sequence.

    :param sequence: DNA sequence needs detecting.
    :param max_homopolymer: maximum length of homopolymer.

    :return: whether the DNA sequence can be considered as valid for DNA synthesis and sequencing.
    """
    if max_homopolymer > len(sequence):
        return True

    missing_segments = ["A" * (1 + max_homopolymer), "C" * (1 + max_homopolymer), "G" * (1 + max_homopolymer),
                        "T" * (1 + max_homopolymer)]

    for missing_segment in missing_segments:
        if missing_segment in "".join(sequence):
            return False
    return True


def cg_content(motif, max_content):
    """
    Check the C and G content of requested DNA sequence.

    :param motif: requested DNA sequence.
    :param max_content: maximum content of C and G, which means GC content is in [1 - max_content, max_content].

    :return: whether the DNA sequence can be considered as valid for DNA synthesis and sequencing.
    """
    return (1 - max_content) <= float(motif.count("C") + motif.count("G")) / float(len(motif)) <= max_content


def fold(motif, min_free_energy):
    """
    Call RNAfold to calculate hairpin MFE of a motif

    :param motif: requested DNA sequence.
    :param min_free_energy: min free energy.

    :return: whether the free energy of DNA sequence is lower than required min free energy.
    """
    if min_free_energy is None:
        return True

    process = subprocess.Popen('echo "%s" | RNAfold --noPS --noGU --noconv -T 59.1' % motif,
                               stdout=subprocess.PIPE, shell=True)
    process.wait()
    if process.returncode == 0:
        line = process.stdout.read().decode().split('\n')[1]
        m = re.search("(\S+)\s+\(\s*(\S+)\)", line)
        if m:
            if min_free_energy > float(m.group(2)):
                return True

    return False
