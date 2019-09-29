#carregar pacotes
import pandas as pd 
import matplotlib as plt

#importar dados
dados = pd.read_csv( "insurance.csv" )

#apresentar os primeiros registros
dados.head()

