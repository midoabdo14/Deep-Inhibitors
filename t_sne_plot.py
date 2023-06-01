# Install RDKit
!pip install rdkit-pypi chemplot

import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from chemplot import Plotter


# Read data
data = pd.read_csv("/content/covid (1).csv") # Replace with your data 


# Create a Plotter object
plotter = Plotter.from_smiles(data["smiles"],target=data["activity"],target_type="C")


# Perform t-SNE dimensionality reduction
plotter.tsne()


# Visualize the t-SNE plot
plotter.visualize_plot()


# Show the plot
plt.show()
