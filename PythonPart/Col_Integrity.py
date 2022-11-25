'''
Created on 24 nov. 2022

@author: Amine
'''


import unittest  
import sys


import PlottingFunctions
import UtilityModule

class testCol(unittest.TestCase):
    def TestColIntegrity(self):
        DF=UtilityModule.LoadDataFrame('C:\\Users\\Amine\\git\\wemanityCodeChallenge\\Data\\chronic_kidney_disease.arff')
        
        Boolean=UtilityModule.CheckColumn(DF,'age')
        self.assertTrue(Boolean, 'The colum in part of the Dataframe')
        
        Boolean=UtilityModule.CheckColumn(DF,'Age')
        self.assertFalse(Boolean, 'The colum in NOT part of the Dataframe')

def plotColumn(DF,col):
    DF[col].plot(kind = 'hist')



