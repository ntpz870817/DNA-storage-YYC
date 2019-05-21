import utils.model_saver as saver
import utils.data_handle as data_handle
import methods.ddyyc as ddyyc

# RULE1 = [1, 0, 0, 1]
# RULE2 = [
#     [1, 0, 1, 0],
#     [1, 0, 1, 0],
#     [0, 1, 0, 1],
#     [0, 1, 0, 1]
# ]
# base_reference=RULE1, current_code_matrix=RULE2
if __name__ == '__main__':
    tool = ddyyc.DDYYC()
    input_matrix, size = data_handle.read_binary_from_all(path="files\\开国大典.mp4")
    dna_motifs = tool.encode(input_matrix, size)
    data_handle.write_dna_file("files\\dna.txt", dna_motifs)
    saver.save_model("models/ddyyc.pkl", tool)
