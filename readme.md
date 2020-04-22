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
- [x] pickle

## Kit Tree Diagram
```html
├── examples                          // Test module
│    ├── files                        // Test files
│    │    ├── Mona Lisa.jpg           // Mona Lisa.jpg
│    │    ├── United Nations Flag.bmp // United Nations Flag.bmp
│    ├── output                       // Generated files from handle
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
When user need to customize YYC transcoding process, an example of command could be:

```python

yyc.YYC(base_reference=[0, 0, 1, 1], current_code_matrix=[[0, 1, 0, 1],[0, 1, 0, 1],[0, 1, 0, 1],[0, 1, 0, 1]],
		support_bases="A", support_spacing=0, max_ratio=0.7, search_count=20)
```

## Method of Application
In the encoding process, we first instantiate the method, and then pass the method and the necessary path into **codec_factory**.

The specific usage is as follows:

```python
import yyc, codec_factory

method = yyc.YYC()

codec_factory.encode(method, input_path="C:\\Mona Lisa.jpg", output_path="C:\\target.dna", model_path="C:\\yyc.pkl")
```

In the decoding process, we first instantiate the method (using path of model file), and then pass the method and the necessary path into **entry**.

The specific usage (using init method) is as follows:

```python
import codec_factory

codec_factory.decode(input_path="C:\\target.dna", output_path="C:\\target.jpg", model_path="C:\\yyc.pkl")
```

## Cite

If you think this repo helps or being used in your research, please consider refer this paper.

[Towards Practical and Robust DNA-based Data Archiving by Codec System Named 'Yin-Yang'](https://www.biorxiv.org/content/10.1101/829721v2)

Thank you!