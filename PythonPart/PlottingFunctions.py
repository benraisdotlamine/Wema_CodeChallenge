'''
Created on 25 nov. 2022

@author: Amine
'''

import matplotlib.pyplot as plt
import seaborn 

def PlotDistribution(DF,var1,Title,Legend):
    plt.figure(figsize=(50,25))
    plt.legend(loc='upper left')
    sb = seaborn.countplot(data = DF, x = var1, hue = 'class')
    sb.legend(title = Title)
    sb.tick_params(labelsize=20)
    plt.setp(sb.get_legend().get_texts(), fontsize='32')
    plt.setp(sb.get_legend().get_title(), fontsize='42')
    sb.set_xlabel('Count',fontsize=40)
    sb.set_ylabel(Legend,fontsize=40)


def PlottingAllColumns(DF,ColName):
    plt.figure(figsize=(40, 25))
    for i,val in enumerate(ColName):
        plt.subplot(5,5,i+1)
        DF[val].hist()
        plt.title(val)
      
    plt.tight_layout()
    plt.show()

def plotColumn(DF,col,k='hist'):
    """
    'line' : line plot (default)
    'bar' : vertical bar plot
    'barh' : horizontal bar plot
    'hist' : histogram
    'box' : boxplot
    'kde' : Kernel Density Estimation plot
    'density' : same as 'kde'
    'area' : area plot
    'pie' : pie plot
    'scatter' : scatter plot
    'hexbin' : hexbin plot
    """
    DF[col].plot(kind = k)

def plotHeatmap(DF, cmap="Greens", annot=True):
    plt.figure(figsize=(10,8))
    DF.corr()
    seaborn.heatmap(DF.corr(),annot=True,cmap="Greens")