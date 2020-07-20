"""
Name: Symmetrical testing for YYC

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): The demo case of Yin-Yang Codec.
"""
from datetime import datetime
import yyc
from utils import data_handle, index_operator

read_file_path = "Exiting the Factory.flv"


if __name__ == "__main__":
    rules = {
        1: ["A", [0, 0, 1, 1], [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]]],
        496: ["A", [0, 1, 0, 1], [[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]]],
        888: ["A", [1, 0, 0, 1], [[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]]],
        1536: ["A", [1, 1, 0, 0], [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]]],
    }

    print("Prepare:")
    input_matrix, size = data_handle.read_binary_from_all(path=read_file_path, segment_length=120, need_log=True)
    input_matrix = index_operator.connect_all(matrix=input_matrix, need_log=True)

    print()
    for rule_index, rule in rules.items():
        method = yyc.YYC(support_bases=rule[0], base_reference=rule[1], current_code_matrix=rule[2],
                         search_count=200, max_homopolymer=4, max_content=0.6)
        for _ in range(5):
            last_time = datetime.now()
            method.encode(matrix=input_matrix, size=size, need_log=True)
            print("rule " + str(rule_index) + " spent " + str(round((datetime.now() - last_time).total_seconds(), 2)) +
                  " seconds.")
            print("\n\n\n\n")
