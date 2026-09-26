import pickle
import pandas as pd
import numpy as np

with open('model/laptop_price_detect','rb') as f:
    model=pickle.load(f)

def predict_output(user_inp: dict):
    input_df=pd.DataFrame([user_inp])
    result=np.exp(model.predict(input_df)).item()
    return result