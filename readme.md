<p align="center">
<img src="https://github.com/ntpz870817/DNA-storage-YYC/blob/master/logo.png" alt="YYC" title="YYC" width="60%"/>
</p>

---

**YYC** is a DNA storage codec algorithm developed by BGI-research. Briefly, it can transcode two binary sequences into one DNA sequence. This algorithm can help to achieve a high-density, high-feasibility DNA storage based on DNA synthesis.

## Environment Configuration
The kit is developed by **Python3.5**.

In addition, the packages we are calling now is as follows:

- [x] sys
- [x] os
- [x] random
- [x] math
- [x] struct
- [x] datetime
- [x] numpy
- [x] pickle

## Kit Tree Diagram
```html
├── test                              // Test module
│    ├── files                        // Test files
│    │    ├── Mona Lisa.jpg           // Mona Lisa.jpg
│    │    ├── United Nations Flag.bmp // United Nations Flag.bmp
│    ├── generated                    // Generated files from handle
│    ├── test_mona_lisa.py            // Run YYC using Mona Lisa.jpg
│    ├── test_united_nations_flag.py  // Run YYC using United Nations Flag.bmp
├── utils                             // Util module
│    ├── data_handle.py               // Conversion of DNA motifs and binary document
│    ├── index_operator.py            // Processing the relationship between index and data
│    ├── log.py                       // Output the logs in console
│    ├── model_saver.py               // Save model to file and load model from file
│    ├── monitor.py                   // Get the progress situation and the time left
│    ├── validity.py                  // Determining whether a DNA sequence is easy or not for sequencing and synthesis
├── codec_factory.py                  // Main calling function
├── yyc.py                            // YYC (Yin-Yang DNA Storage Code)
├── README.md                         // Description document of kit
```

## Introduction of Yin-Yang Code
Yin-Yang Code is the algorithm describes the collection of derivative rules reported by Ping et. al.
Six hyper-parameters are included in this method: base_reference, current_code_matrix, support_bases, support_spacing,max_ratio, and search_count.
bse_referece: Yang rule, correspondence between base and bit data in the binary segment I. The default value is Rule 495, [0, 1, 0, 1].
current_code_matrix: Yin rule, correspondence between base and bit data in the binary segment II. The default value is Rule 495, [[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]].
support_bases: indicates the virtual base used for both encoding and decoding before real information, the default value is 'A'.
support_spacing: indicates the spacing between support nucleotide and current nucleotide. If support nucleotide is directly one position before current nucleotide, the spacing would be 0. If support_bases = 'AA', then the supporting_spacing would be 1.
max_ratio: indicates the criteria of determine whether a binary segment is considered to be 'good' or 'bad' for incorporation. For example, the default value of max_ratio is 0.8, which means that if '0' or '1' exceeds 80% of the binary segment, the segment will be considered to be 'bad' for incoporation.
search_count: indicates how many times the program will do to search for incorporation. This parameter is used for avoid infinite loop and save time. The default value is 2.
When user need to customize YYC transcoding process, an example of command could be:

```python

	yyc.YYC(base_reference=[0, 0, 1, 1], current_code_matrix=[[0, 1, 0, 1],[0, 1, 0, 1],[0, 1, 0, 1],[0, 1, 0, 1]],
		support_bases="AC", support_spacing=1, max_ratio=0.7, search_count=20)
```

## Method of Application
In the encoding process, we first instantiate the method, and then pass the method and the necessary path into **codec_factory**.

The specific usage is as follows:

```python
import yyc, codec_factory

method = yyc.YYC()

codec_factory.encode(method, input_path="C:\\init.mp4", output_path="C:\\target.dna", model_path="C:\\yyc.pkl")
```

In the decoding process, we first instantiate the method (using path of model file), and then pass the method and the necessary path into **entry**.

The specific usage (using init method) is as follows:

```python
import codec_factory

codec_factory.decode(input_path="C:\\target.dna", output_path="C:\\target.mp4", model_path="C:\\yyc.pkl")
```

## Cite

If you think this repo helps or being used in your research, please consider refer this paper.

[Towards Practical and Robust DNA-based Data Archiving by Codec System Named 'Yin-Yang'](https://www.biorxiv.org/content/10.1101/829721v2)

Thank you!

````
@article{ping2019towards,
  title={Towards Practical and Robust DNA-based Data Archiving by Codec System Named 'Yin-Yang'},
  author={Ping, Zhi and Chen, Shihong and Huang, Xiaoluo and Zhu, Sha and Chai, Chen and Zhang, Haoling and Lee, Henry H and Zhou, Guangyu and Chiu, Tsan-Yu and Chen, Tai and others},
  journal={bioRxiv},
  pages={829721},
  year={2019},
  publisher={Cold Spring Harbor Laboratory}
}
````