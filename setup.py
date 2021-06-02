from setuptools import setup

setup(
    name='yyc',
    version='1.0',
    author='Haoling Zhang, Zhi Ping',
    author_email='zhanghaoling@genomics.cn',
    maintainer='BGI-Research',
    url='https://github.com/ntpz870817/DNA-storage-YYC',
    description='Yin-Yang Code implementation',
    long_description='Yin-Yang Code is a DNA storage codec algorithm developed by BGI-research. ' +
                     'Briefly, it can transcode two binary sequences into one DNA sequence. ' +
                     'This algorithm can help to achieve a high-density, high-feasibility DNA storage.',
    packages=['yyc', 'yyc/utils'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        'Topic :: Scientific/Engineering'
    ]
)
