import utils.model_saver as saver
import utils.data_handle as data_handle

RULE1 = [0, 0, 1, 1]
RULE2 = [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]

if __name__ == '__main__':
    tool = saver.load_model("models/yyc.pkl")
    dna_motifs = data_handle.read_dna_file("files\\dna.txt")
    output_matrix = tool.decode(dna_motifs)
    data_handle.write_all_from_binary("files\\target.mp4", output_matrix, tool.file_size)
