# Install rdkit
!pip install rdkit-pypi

from rdkit.Chem import AllChem as Chem
from rdkit.Chem import PandasTools
from rdkit import DataStructs
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Read datafile
datafile = pd.read_csv('/datafile')  # Replace with the path to your datafile
datafile.head()


# Convert smiles to Molecule
PandasTools.AddMoleculeColumnToFrame(datafile, 'smiles', 'Molecule', includeFingerprints=True)
print([str(x) for x in datafile.columns])


# Visualize molecules
PandasTools.FrameToGridImage(datafile, column='Molecule', molsPerRow=4, subImgSize=(150, 150))
datafile = datafile.dropna(subset=['Molecule'])  # Remove rows with None values in 'Molecule' column


# Calculate molecular fingerprints
mollist = []
for mol in datafile['Molecule']:
    try:
        fp = Chem.GetMorganFingerprintAsBitVect(mol, 2)
        mollist.append(fp)
    except:
        mollist.append(None)
datafile['mfp2'] = mollist


# Calculate Tanimoto similarity
for r in datafile.index:
    fp1 = datafile.at[r, 'mfp2']
    colname = datafile.at[r, 'ID']
    simlist = []
    for mol in datafile['Molecule']:
        try:
            fp = Chem.GetMorganFingerprintAsBitVect(mol, 2)
            sim = DataStructs.TanimotoSimilarity(fp1, fp)
            simlist.append(sim)
        except:
            simlist.append(None)
    datafile[colname] = simlist


# Drop unnecessary columns
newdatafile = datafile.drop(['smiles', 'Molecule', 'mfp2'], axis=1)
newdatafile.drop(['ID'], axis=1, inplace=True)


# Heatmap visualization
cm = sns.light_palette("red", as_cmap=True)
vis = newdatafile.style.background_gradient(cmap=cm)


# Plot heatmap
ax = sns.heatmap(newdatafile, xticklabels=False, yticklabels=False)
plt.xlabel('Compounds')
plt.ylabel('Compounds')
plt.savefig('ax.png')


# Display the processed dataframes
print(newdatafile)
