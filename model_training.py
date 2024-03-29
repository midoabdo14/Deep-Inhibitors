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
splitter= dc.splits.RandomStratifiedSplitter()
train_dataset,val_dataset,test_dataset = splitter.train_valid_test_split(dataset)
print(len(train_dataset))
print(len(val_dataset))
print(len(test_dataset))



# Build and train model  
metric = dc.metrics.Metric(dc.metrics.roc_auc_score)
model = dc.models.GraphConvModel(n_tasks=len(file_tasks),batch_size =64,dense_layer_size=256,learning_rate=0.0001)
model.fit(train_dataset, nb_epoch=20)



# Evaluate model 
train_score = model.evaluate(train_dataset, [metric], transformers)
val_score = model.evaluate(val_dataset, [metric], transformers)
test_score = model.evaluate(test_dataset,[metric],transformers)
print(f" train_score: {train_score}")
print(f" val_score: {val_score}")
print(f" test_score: {val_score}")
