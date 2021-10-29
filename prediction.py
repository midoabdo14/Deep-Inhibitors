# Import deepchem
!wget -c https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
!chmod +x Anaconda3-2019.10-Linux-x86_64.sh
!bash ./Anaconda3-2019.10-Linux-x86_64.sh -b -f -p /usr/local
!conda install -y -c deepchem -c rdkit -c conda-forge -c omnia deepchem-gpu=2.3.0
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
import deepchem as dc

# Import other libraries
import numpy as np
import random
import tensorflow as tf
np.random.seed(123)
tf.random.set_random_seed(123)
import pandas as pd

# Explore data
dr=pd.read_csv('/data/example.csv')  # you can replace this path with your own data file path
dr.head()

# Prepare data
dr_tasks =['predict']
featurizer = dc.feat.ConvMolFeaturizer()
dataset_file = '/data/example.csv'  # you can replace this path with your own data file path
loader = dc.data.CSVLoader(
         tasks= dr_tasks,smiles_field="smiles", featurizer=featurizer) 
rdtest = loader.featurize(dataset_file,shard_size=8192)

from deepchem.models import GraphConvModel

model= GraphConvModel(model_dir='/trained model',n_tasks=1)
model.restore()

prediction1=model.predict(rdtest)

# save model prediction
# prediction=predcition.reshape(3897,2)
pd.DataFrame(prediction).to_csv("result.csv", index = None)
