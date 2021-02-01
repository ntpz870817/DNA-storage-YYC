import codec_factory
import yyc
from utils import data_handle

read_file_path = "./files/Mona Lisa.jpg"
dna_path = "./output/mona_lisa.dna"
model_path = "./output/mona_lisa.pkl"
write_file_path = "./output/output_mona_lisa.jpg"

if __name__ == "__main__":
    [support_base, rule1, rule2] = ["A", [0, 1, 0, 1], [[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]]]
    tool = yyc.YYC(support_bases=support_base, base_reference=rule1, current_code_matrix=rule2,
                   search_count=100, max_homopolymer=4, max_content=0.6)
    codec_factory.encode(
        method=tool,
        input_path=read_file_path,
        output_path=dna_path,
        model_path=model_path,
        need_index=True,
        need_log=True
    )
    del tool
    codec_factory.decode(
        model_path=model_path,
        input_path=dna_path,
        output_path=write_file_path,
        has_index=True,
        need_log=True
    )

    # compare two file
    matrix_1, _ = data_handle.read_binary_from_all(read_file_path, 120, False)
    matrix_2, _ = data_handle.read_binary_from_all(write_file_path, 120, False)
    print("source digital file == target digital file: " + str(matrix_1 == matrix_2))
