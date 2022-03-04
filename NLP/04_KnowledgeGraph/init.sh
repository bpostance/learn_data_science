#!/usr/bin/env bash

# setup python env
conda env create -f ./environment.yaml
conda activate py37

# install spacy large model 700mb
pip --default-timeout=1000 install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.1.0/en_core_web_lg-2.1.0.tar.gz

# install neuralcoref from source
git clone https://github.com/huggingface/neuralcoref.git
cd neuralcoref
pip install -r requirements.txt
pip install -e .
cd ..
rm -rf neuralcoref