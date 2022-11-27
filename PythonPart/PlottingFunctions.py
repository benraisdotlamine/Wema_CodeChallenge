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
    

def NumericalValueDistribution(CKD_dataframe,NumericalColumns):
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15,15))
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle('Distribution des attributs numeriques')

    for ax, feats in zip(axes.flatten(), NumericalColumns):
        seaborn.histplot(CKD_dataframe[feats],ax=ax, kde=True)

def NominalValueDistribution(CKD_dataframe,NominalCols):
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15,15))
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle('Distribution des attributs nominal')

    for ax, feats in zip(axes.flatten(), NominalCols):
        seaborn.countplot(CKD_dataframe[feats],ax=ax)


def violin(col):
    fig = px.violin(df, y=col, x="class", color="class", box=True, points="all", hover_data=df.columns)
    return fig.show()

def scatters(col1,col2):
    fig = px.scatter(df, x=col1, y=col2, color="classification")
    fig.show()