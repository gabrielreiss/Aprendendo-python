#carregar pacotes
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl

#importar dados
dados = pd.read_csv( "insurance.csv" )

#transformar dados
dados["region"].unique()

#dados["smoker2"]

#apresentar os primeiros registros
dados.head()

#verificar NA
dados.isnull().sum()

#correlações
dados.corr()

#plot test
plt.plot(dados["age"],dados["charges"],'o');plt.show()


