import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np

#Crea subsessions passant un interval de hores així com un dataframe
def create_subsesh(f,hores):
    f.sort_values(by=['sessionId','ts'])
    llisteta = [(f[f['sessionId']==session]['ts'] - np.insert(f[f['sessionId']==session]['ts'].values,0,0,axis=0)[:-1]).values for session in pd.unique(f['sessionId'])]
    llisteta = [item for sublist in llisteta for item in sublist]
    f['dif'] = llisteta
    cut_dif = pd.Timedelta(hores,'h')
    i=0
    l=[]
    for sessionId in pd.unique(f['sessionId']):
        for event in f[f['sessionId'] == sessionId].values:
            if event[-1]>cut_dif:
                i=i+1
            l.append(i)
    f['subsession'] = l


#Crea dia, mes i dia de la setmana passant un dataframe

def create_date_features(f):
    f.loc[:, 'month'] = f['ts'].dt.month
    f.loc[:, 'weekofyear'] = f['ts'].dt.weekofyear
    f.loc[:, 'dayofweek'] = f['ts'].dt.dayofweek
