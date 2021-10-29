# Deep learning based screening for anti-SARS-CoV-2 inhibitors
Using graph convolutional network for molcular properties prediction of anti-SARS-COV-2 inhibitors.

# Data 
- Data to train the model exist as SMILE strings format, labelled as 0 (non active) or 1 (active compounds) 
- Saved as csv file in the data directory

# Train Model
- To train model using our data
- Clone model to your working directory
```
cd Inhbitors
!python model training.py
```

- To train model using your own data,replace data file path in model training.py file with your data path

# Model prediction
- To make prediction in new dataset, replace data file path in prediction.py file with your data path 
- To test model on the example file 
``` 
!python prediction
```
