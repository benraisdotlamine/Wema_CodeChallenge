'''
Created on 24 nov. 2022

@author: Amine
'''
import numpy as np
import pandas as pd
from scipy.io.arff import loadarff 

def LoadDataFrame(Path):
    DataExtraction = loadarff(Path)
    DF= pd.DataFrame(DataExtraction[0])
    #CKD_DataDescription=DataExtraction[1]
    return DF

def CheckColumn(DF,Col):
    if Col in DF.columns.values.tolist():
        return True
    return False



def getAllNumericCol(DF):
    TransformedDF=DF.applymap(np.isreal)
    ListOfNumericalCol=[]
    for col in TransformedDF:
        if any(TransformedDF[col])==True:
            ListOfNumericalCol.append(col)
 
    return ListOfNumericalCol



    