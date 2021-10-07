# # Install RDKit. Takes 2-3 minutes
# %%capture
# !wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
# !chmod +x Miniconda3-latest-Linux-x86_64.sh
# !time bash ./Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local
# !time conda install -q -y -c conda-forge python=3.7
# !time conda install -q -y -c conda-forge rdkit=2020.09.02

import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem import PandasTools
import numpy as np
import pandas as pd

data = pd.read_csv('test.csv',low_memory=False)

data.head()

PandasTools.AddMoleculeColumnToFrame(data,'smiles','Molecule')
data

from IPython.core.display import HTML

html = data.to_html()

#write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
