import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def get_explore_data():
    df = pd.read_csv('train_data.csv')
    return df

def prep_data(df, features):
    df = df[features]
    return df

def split_data(df, test_size=0.15):
    '''
    Takes in a data frame and the train size
    It returns train, validate , and test data frames
    with validate being 0.05 bigger than test and train has the rest of the data.
    '''
    train, test = train_test_split(df, test_size = test_size , random_state=27)
    train, validate = train_test_split(train, test_size = (test_size + 0.05)/(1-test_size), random_state=27)
    
    return train, validate, test