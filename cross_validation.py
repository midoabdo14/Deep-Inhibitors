# Install libraries
!pip install deepchem
import deepchem as dc
from deepchem.models import GraphConvModel
import numpy as np
import random
import tensorflow as tf
import pandas as pd
np.random.seed(123)


# Load data 
file=pd.read_csv('/content/covid.csv')  # you can replace this path with your own data file path
file.head()


# Data featurization and transformation 
file_tasks =['activity']
featurizer = dc.feat.ConvMolFeaturizer()
dataset_file = '/content/covid.csv'  # you can replace this path with your own data file path
loader = dc.data.CSVLoader(
        tasks= file_tasks, smiles_field="smiles", featurizer=featurizer) 
dataset = loader.featurize(dataset_file,shard_size=8192)
transformers= [
               dc.trans.BalancingTransformer(
                dataset=dataset
               )            
]

for transformer in transformers:
  dataset= transformer.transform(dataset)


# Data splitting 
splitter=dc.splits.RandomSplitter()
split_datas = splitter.k_fold_split(dataset,5)


# Build and train model  
metric = dc.metrics.Metric(dc.metrics.roc_auc_score)

validation_scores = []
train_scores = []
learning_rate = dc.models.optimizers.ExponentialDecay(0.0002, 0.9, 1000)
for train_set, val_set in split_datas:
    model = dc.models.GraphConvModel(len(file_tasks),batch_size =64,droupout=0,dense_layer_size=256,learning_rate=learning_rate,model_dir='trained model')
    callback = dc.models.ValidationCallback(val_set, 1000, metric)
    model.fit(train_set, nb_epoch = 20,callbacks=callback)
    train_score = model.evaluate(train_set, [metric], transformers)
    train_scores.append(list(train_score.values()).pop()) 
    valid_score = model.evaluate(val_set, [metric], transformers)
    validation_scores.append(list(valid_score.values()).pop())
  
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

