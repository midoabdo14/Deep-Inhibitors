# Deep learning based screening for anti-SARS-CoV-2 inhibitors
Using graph convolutional network for molcular properties prediction of anti-SARS-COV-2 inhibitors.
![image](https://github.com/midoabdo14/Deep-Inhibitors/assets/91239112/98f8c44c-b082-455c-969c-34cc0e6eee33)


# Data 
- Data to train the model exist as SMILE strings format, labeled as 0 (non active) or 1 (active compounds) 
- Saved as csv file in the data directory

# Train Model
- To train model using our data, clone model to your working directory and run 
```
cd Inhbitors
!python model_training.py
```

- To train model using your own data, replace data file path in model training.py file with your own data path

# Model prediction
- To make prediction in new dataset using our model, replace data file path in prediction.py file with your own data path 
- To test model on the example file, run
``` 
!python model_prediction.py
```
