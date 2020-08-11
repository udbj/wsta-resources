# wsta-project

Used Docker to run PyLucene. [repo: coady/pylucene]

Download and build fairseq:

git clone https://github.com/pytorch/fairseq
cd fairseq
pip install --editable ./

In Python interactive shell:

from fairseq load libbleu
import torch
torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')

After it downloads the model, close the Python shell. 
Replace all files in ~/.cache/hub/pytorch_fairseq_master/ with the ones in the downloaded fairseq folder.

Run simcheck.py from bash shell.
