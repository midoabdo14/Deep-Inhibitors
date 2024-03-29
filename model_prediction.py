# Install libraries
!pip install deepchem
import deepchem as dc
from deepchem.models import GraphConvModel
import numpy as np
import random
import tensorflow as tf
import pandas as pd
np.random.seed(123)


# Read and process example file 
dr=pd.read_csv('/data/example.csv')  # you can replace this path with your own data file path
dr.head()
dr_tasks =['predict']
featurizer = dc.feat.ConvMolFeaturizer()
dataset_file = '/data/example.csv'  # you can replace this path with your own data file path
loader = dc.data.CSVLoader(
         tasks= dr_tasks,smiles_field="smiles", featurizer=featurizer) 
rdtest = loader.featurize(dataset_file,shard_size=8192)


# Load trained model 
model= GraphConvModel(model_dir='/content/model',n_tasks=1)
model.restore()


# Make prediction and save csv file  
prediction1=model.predict(rdtest)
prediction=prediction1.reshape(5,2)   # reshape based on your data
pd.DataFrame(prediction).to_csv("result.csv", index = None)
