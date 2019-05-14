"""
Name: Main (General Program Entry)

Creators: HaoLing ZHANG (BGI-Research)[Version 1]

Current Version: 1

"""

import utils.data_handle as data_handle
import methods.yyc as yyc
# import methods.ddyyc as ddyyc
import utils.model_saver as saver

RULE1 = [0, 0, 1, 1]
RULE2 = [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]

if __name__ == '__main__':
    tool = yyc.YYC(base_reference=RULE1, current_code_matrix=RULE2)
    # tool = ddyyc.DDYYC(base_reference=RULE1, current_code_matrix=RULE2)
    input_matrix, size = data_handle.read_binary_from_all()
    dna_motifs = tool.encode(input_matrix, size)
    data_handle.write_dna_file(dna_motifs)
    saver.save_model("models/yyc.pkl", tool)

    tool = saver.load_model("models/yyc.pkl")
    dna_motifs = data_handle.read_dna_file()
    output_matrix = tool.decode(dna_motifs)
    data_handle.write_all_from_binary(output_matrix, size)
