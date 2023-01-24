import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

features = ['climateregions__climateregion', 'elevation__elevation', 'lat', 'lon', 'startdate',
                 'contest-pevpr-sfc-gauss-14d__pevpr','contest-precip-14d__precip','contest-pres-sfc-gauss-14d__pres',
                 'contest-prwtr-eatm-14d__prwtr','contest-rhum-sig995-14d__rhum','contest-slp-14d__slp',
                 'contest-tmp2m-14d__tmp2m','contest-wind-h10-14d__wind-hgt-10','contest-wind-h100-14d__wind-hgt-100',
                 'contest-wind-h500-14d__wind-hgt-500','contest-wind-h850-14d__wind-hgt-850','contest-wind-uwnd-250-14d__wind-uwnd-250',
                 'contest-wind-uwnd-925-14d__wind-uwnd-925','contest-wind-vwnd-250-14d__wind-vwnd-250',
                 'contest-wind-vwnd-925-14d__wind-vwnd-925']

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