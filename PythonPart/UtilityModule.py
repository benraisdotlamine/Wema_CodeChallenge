'''
Created on 25 nov. 2022

@author: Amine
'''
import numpy as np
import pandas as pd
from scipy.io.arff import loadarff 

#function used to load the dataset
def LoadDataFrame(Path):
    DataExtraction = loadarff(Path)
    DF= pd.DataFrame(DataExtraction[0])
    return DF

#checks if the column exists in the dataframe (used in the unit test)
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





    