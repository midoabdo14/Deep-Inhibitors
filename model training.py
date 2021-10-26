# Import deepchem
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
import pandas as pd
np.random.seed(123)
tf.random.set_random_seed(123)

# Read datafile 
file=pd.read_csv('data/covid.csv')
file_tasks =['activity']



featurizer = dc.feat.ConvMolFeaturizer()
dataset_file = 'data/covid.csv'
loader = dc.data.CSVLoader(
        tasks= file_tasks, smiles_field="smiles", featurizer=featurizer) 
dataset = loader.featurize(dataset_file,shard_size=8192)

transformers= [
               dc.trans.BalancingTransformer(
                transform_w=True, dataset=dataset
               )            
]

for transformer in transformers:
  dataset= transformer.transform(dataset)

splitter=dc.splits.RandomSplitter(dataset)
split_datas = splitter.k_fold_split(dataset,5)

from deepchem.models import GraphConvModel
metric = dc.metrics.Metric(
    dc.metrics.roc_auc_score, np.mean, mode="classification")

# conduct cross-validation
validation_scores = []
train_scores = []
learning_rate = dc.models.optimizers.ExponentialDecay(0.0002, 0.9, 1000)
for train_set, val_set in split_datas:
    model = dc.models.GraphConvModel(len(file_tasks),batch_size =64,droupout=0,dense_layer_size=256,learning_rate=learning_rate,model_dir='model5')
    callback = dc.models.ValidationCallback(val_set, 1000, metric)
    model.fit(train_set, nb_epoch = 20,callbacks=callback)
    train_score = model.evaluate(train_set, [metric], transformers)
    train_scores.append(list(train_score.values()).pop()) 
    valid_score = model.evaluate(val_set, [metric], transformers)
    validation_scores.append(list(valid_score.values()).pop())    
       
    
# print out the results of cross validation    
print("===========Final Results===========")
cross_train_score = 0    
for val in train_scores:
    cross_train_score += val
cross_train_score = cross_train_score/5
print("cross_train_score: ")
print(cross_train_score)
cross_validation_score = 0    
for val in validation_scores:
    cross_validation_score += val
cross_validation_score = cross_validation_score/5
print("cross_validation_score: ")
print(cross_validation_score)