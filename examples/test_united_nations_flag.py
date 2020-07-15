import codec_factory
import yyc
from utils import data_handle
from utils.rule_set import get_yyc_rule_by_index

read_file_path = "./files/United Nations Flag.bmp"
dna_path = "./output/united_nations_flag.dna"
model_path = "./output/united_nations_flag.pkl"
write_file_path = "./output/output_united_nations_flag.jpg"

if __name__ == "__main__":
    [support_base, rule1, rule2] = get_yyc_rule_by_index(888, True)
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
