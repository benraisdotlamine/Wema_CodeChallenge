'''
Created on 25 nov. 2022

@author: Amine
'''

import pandas as pd
from sklearn import preprocessing



def RelationshipInNumbers(DF, attribute1, attribute2):
    
    try :
        float(DF.at[1,attribute2])
        NumericValue=True
        #print('numerical value')
    except:
        NumericValue=False
        #print('not numerical value')
        
    if NumericValue:
        #print(DF.groupby([attribute1])[attribute2].agg(['count','mean','min','max','var']))
        return DF.groupby([attribute1])[attribute2].agg(['count','mean','min','max','var'])
    else : 
        Dict={}
        for C in DF[attribute1].unique():
            for V in DF[attribute2].unique():
                Dict[(C,V)]=len(DF[(DF[attribute1]==C) & (DF[attribute2]==V)])
        return pd.DataFrame.from_dict(Dict,orient='index')
       




def Normalize_sklearn(DF,ColName):
    for col in ColName:
        DF[col]= preprocessing.LabelEncoder().fit_transform(DF[col])
    x = DF.values 
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    DF = pd.DataFrame(x_scaled)


def normalize_function_mean(DF, col):
    
    DF[col] = (DF[col]-DF[col].mean())/(DF[col].std())

    return DF

def normalize_function_minmax(DF, col):
    DF[col] = (DF[col]-DF[col].min())/(DF[col].max()-DF[col].min())
    

    return DF


def FillAllMissingValues(DF,Attribute,BinaryClassArray):
    for index in range(len(DF)):
        if pd.isnull(DF.at[index,Attribute]) :
            if DF.at[index,'class']==BinaryClassArray[0]:
                DF.at[index,Attribute]=DF[DF['class']==BinaryClassArray[0]].dropna().sample(1)[Attribute].to_numpy()[0]
            else : 
                DF.at[index,Attribute]=DF[DF['class']==BinaryClassArray[1]].dropna().sample(1)[Attribute].to_numpy()[0]


def CorrelationBetweenVariables(DF,Var1, Var2):
    corr_suited = DF[[Var1, Var2]]
    return (corr_suited[corr_suited[Var1] == 'ckd'].groupby([Var2]).size().reset_index(name = 'count')).corr()


def FillMissingValues(DF,printing=False):
  for col in DF.columns.values.tolist():
    if printing:
      print(col)
    AnalyseFunctions.FillAllMissingValues(DF,col,['ckd','notckd'])