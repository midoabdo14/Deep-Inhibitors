# Install rdkit
!pip install rdkit-pypi
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from rdkit.Chem import Draw
from rdkit import DataStructs

# Install other libraries
import numpy
import seaborn as sns
import matplotlib
import pandas as pd
# %matplotlib inline

# Read datafile
datafile = pd.read_csv('datafile path')
datafile.head()

# Convert smiles to Molecule
PandasTools.AddMoleculeColumnToFrame(datafile,'smiles', 'Molecule' , includeFingerprints=True)
print([str(x) for x in datafile.columns])

# Visulize molecules
PandasTools.FrameToGridImage(datafile,column= 'Molecule', molsPerRow=4,subImgSize=(150,150))

# Get molecular fingerprint
mollist = [] 
for mol in datafile['Molecule']:
    fp = Chem.GetMorganFingerprintAsBitVect( mol,2 )
    mollist.append(fp)

datafile['mfp2']=mollist

fp1=datafile.at[0,'mfp2']
fp2=datafile.at[1,'mfp2']

# Tanimoto similarity

for r in datafile.index:
    fp1 = datafile.at[r,'mfp2']
    colname = datafile.at[r,'ID']
    simlist = []
    for mol in datafile['Molecule']:
        fp = Chem.GetMorganFingerprintAsBitVect(mol,2)
        sim = DataStructs.TanimotoSimilarity(fp1,fp)
        simlist.append(sim)
    datafile[colname]=simlist

datafile.head(1)

newdatafile = datafile.drop(['smiles',"Molecule",'mfp2'], axis=1)
newdatafile

# Heat map visualization
cm = sns.light_palette("red", as_cmap=True)
vis = newdatafile.style.background_gradient(cmap=cm)
vis

newdatafile2 = newdatafile.drop(['ID'],axis = 1)

newdatafile2

ax = sns.heatmap(newdatafile2, xticklabels=x_axis_labels, yticklabels=y_axis_labels)
plt.xlabel('Compounds')
plt.ylabel('Compounds')
plt.savefig('ax.png')
