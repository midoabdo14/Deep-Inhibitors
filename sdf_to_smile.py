#Install RDKit. Takes 2-3 minutes
%%capture
!wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
!chmod +x Miniconda3-latest-Linux-x86_64.sh
!time bash ./Miniconda3-latest-Linux-x86_64.sh -b -f -p /usr/local
!time conda install -q -y -c conda-forge python=3.7
!time conda install -q -y -c conda-forge rdkit=2020.09.02

import rdkit

import sys
from rdkit import Chem

def converter(file_name):
    sppl = Chem.SDMolSupplier('data/file.sdf')
    outname = file_name.replace("sdf", "txt")
    out_file = open(outname, "w")
    for mol in sppl:
        if mol is not None:# some compounds cannot be loaded.
            smi = Chem.MolToSmiles(mol)
            out_file.write(f"{smi}\n")
    out_file.close()
if __name__ == "__main__":
    converter(sys.argv[1])

