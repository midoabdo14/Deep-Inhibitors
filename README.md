# Deep learning based screening for anti-SARS-CoV-2 inhibitors
Using graph convolutional network for molcular properties prediction of anti-SARS-COV-2 inhibitors.

# Data 
- Data to train the model exist as SMILE strings format, labelled as 0 (non active) or 1 (active compounds) 
- Saved as csv file in the data directory

# Train Model
- Clone model to your working directory
```
cd Inhbitors
!python model training.py
```

# Model prediction
- To make prediction in new dataset, replace file directory in prediction.py with your data directory 
- To run example file 
``` 
!python prediction
```
