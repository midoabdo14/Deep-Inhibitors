# -*- coding: utf-8 -*-
"""NCATS invest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VuFWOaF_a53Kr14ZGY-HYWt5dZSPB87s
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
!wget -c https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
!chmod +x Anaconda3-2019.10-Linux-x86_64.sh
!bash ./Anaconda3-2019.10-Linux-x86_64.sh -b -f -p /usr/local
!conda install -y -c deepchem -c rdkit -c conda-forge -c omnia deepchem-gpu=2.3.0
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
import deepchem as dc

import numpy as np
import random
import tensorflow as tf
random.seed(123)
np.random.seed(123)
tf.random.set_random_seed(123)

from google.colab import files
uploaded = files.upload()

import pandas as pd
dr=pd.read_csv('invest.csv')

dr.head()

import deepchem as dc
dr_tasks =['predict']
featurizer = dc.feat.ConvMolFeaturizer()
dataset_file = 'invest.csv'
loader = dc.data.CSVLoader(
         tasks= dr_tasks,smiles_field="smiles", featurizer=featurizer) 
rdtest = loader.featurize(dataset_file,shard_size=8192)

from deepchem.models import GraphConvModel

model1= GraphConvModel(model_dir='/content/model1',n_tasks=1)
model1.restore()

c

prediction1=model1.predict(rdtest)
prediction2=model2.predict(rdtest)

predcition = (prediction1+prediction2)/2

prediction=predcition.reshape(3897,2)
pd.DataFrame(prediction).to_csv("resultnew.csv", index = None)