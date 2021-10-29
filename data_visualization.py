# install Chemplot library
!pip install chemplot

# Install rdkit 
!pip install rdkit-pypi

import pandas as pd
data = pd.read_csv("active compound.csv")



import chemplot as cp
plotter = cp.Plotter.from_smiles(data["smiles"], target=data["activity"], target_type="C")

plotter.tsne()

import matplotlib.pyplot as plt
plotter.visualize_plot()
plt.show()
