<p align="center">
<img src="https://github.com/ntpz870817/DNA-storage-YYC/blob/master/logo.png" alt="YYC" title="YYC" width="60%"/>
</p>

---

**YYC** is a DNA storage codec algorithm developed by BGI-research.
Briefly, it can transcode two binary sequences into one DNA sequence.
This algorithm can help to achieve a high-density, high-feasibility DNA storage based on DNA synthesis.

Prior to utilizing this repository, we kindly request that you possess a fundamental comprehension of DNA-based data storage. 
An inappropriate communication case can be seen [here](https://github.com/ntpz870817/DNA-storage-YYC/issues/4) for reference. 
Should you have any inquiries, please don't hesitate to reach out to us via either [Dr. Zhi Ping](pingzhi@genomics.cn), [Mr. Haoling Zhang](zhanghaoling@genomics.cn) or [Dr. Yue Shen](shenyue@genomics.cn).

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
├── yyc
│    ├── utils                        // Util module
│    │    ├── data_handle.py          // Conversion of DNA motifs and binary document
│    │    ├── index_operator.py       // Processing the relationship between index and data
│    │    ├── log.py                  // Output the logs in console
│    │    ├── model_saver.py          // Save model to file and load model from file
│    │    ├── monitor.py              // Get the progress situation and the time left
│    │    ├── validity.py             // Determining whether a DNA sequence is easy or not for sequencing and synthesis
│    ├── pipeline.py                  // Main calling function
│    ├── scheme.py                    // YYC (Yin-Yang DNA Storage Code)
├── README.md                         // Description document of kit
```

## Introduction of Yin-Yang Code
Yin-Yang Code is the algorithm describes the collection of derivative rules reported by Ping et. al.

The users could install this package by 'pip install yyc'.
When you have finished installing the package, the sample program in [folder](https://github.com/ntpz870817/DNA-storage-YYC/tree/master/examples) could be run to make sure the package is correct.

We strongly suggest using Python IDE (such as PyCharm) to complete your transcoding task, please see the examples [here](https://github.com/ntpz870817/DNA-storage-YYC/tree/master/examples).
The command line is relatively long and hard to customize, for example:

In the encoding process
```python
python
>>> from yyc import pipeline
>>> from yyc import scheme
>>> pipeline.encode(method=scheme.YYC(support_bases="A", base_reference=[0, 1, 0, 1], current_code_matrix=[[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]], search_count=100, max_homopolymer=4, max_content=0.6), input_path="./files/Mona Lisa.jpg", output_path="./output/mona_lisa.dna", model_path="./output/yyc.pkl", need_index=True, need_log=True)
```

In the decoding process
```python
python
>>> from yyc import pipeline
>>> pipeline.decode(model_path="./output/yyc.pkl",input_path="./output/mona_lisa.dna", output_path="./output/output_mona_lisa.jpg", has_index=True, need_log=True)
```


## Citing

If you think this repo helps or being used in your research, please consider refer this paper.

[Towards practical and robust DNA-based data archiving using the yin--yang codec system](https://www.nature.com/articles/s43588-022-00231-2)

````
@article{ping2022towards,
  title={Towards practical and robust DNA-based data archiving using the yin--yang codec system},
  author={Ping, Zhi and Chen, Shihong and Zhou, Guangyu and Huang, Xiaoluo and Zhu, Sha Joe and Zhang, Haoling and Lee, Henry H and Lan, Zhaojun and Cui, Jie and Chen, Tai and others},
  journal={Nature Computational Science},
  pages={234--242},
  year={2022},
  volume={2},
  number={4},
  publisher={Nature Publishing Group}
}
````

Thank you!
