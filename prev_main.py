import pandas as pd
import matplotlib.pyplot as pyplot 
import seaborn as sns
import numpy as np

pd.options.display.max_rows = 99

dataframe = pd.read_excel('dataset.xlsx')

# body= dataframe.shape
# print(body)

# body = dataframe.tail
# print(body)

#dataframe.info()


def drop_columns(data):

    for i in data.columns:
        percentual=(data[i].isnull().sum() / len(data['Patient ID'])) *100

        if percentual > 92: 
            
            new_data = data.drop(i, axis='columns')
            data = new_data    
    new_data = data
    
    return new_data
    
new_data = drop_columns(dataframe)
print('???????????????')
#print(new_data)


# # for i in range(49):
#     #  dataframe[dataframe.columns[i]] = dataframe[dataframe.columns[i]].fillna((dataframe.columns[i].median()))

# new_data['Hematocrit'] = new_data['Hematocrit'].fillna((new_data['Hematocrit'].median()))



# # info = dataframe.groupby(['Hematocrit']).size()
# # print(info)  

  

# null = new_data['Hematocrit'].isnull().sum()
# null = new_data['Respiratory Syncytial Virus'].isnull().sum()
# null = new_data.isnull().sum()
# print(null)


# if percen > 92:
#     new_data = new_data.drop('Indirect Bilirubin',axis='columns')
# def normalizacao_float(data):
#         for i in data.columns
#         print()
    
#     return

def relativando_dados_flutuantes(data): 
    dado_tratado = data
    trat = data.select_dtypes(include='float64')
    
    for i in trat.columns:
       # print(i)
        dado_tratado[i] = dado_tratado[i].fillna((dado_tratado[i].median()))
        #print(dado_tratado[i])
    return dado_tratado

def relativando_dados_objects(data):
    dado_tratado = data
    trat = data.select_dtypes(include='object')
    
    for i in trat.columns:
        #print(i)
        dado_tratado[i] = dado_tratado[i].fillna('sem daddos', inplace = True)
    
    return dado_tratado

new_data['Hemoglobin'] = new_data['Hemoglobin'].fillna((new_data['Hemoglobin'].median()))
kk =  new_data.select_dtypes(include='float64')

data_tratado_float = relativando_dados_flutuantes(new_data)
data_frame_tratado = relativando_dados_objects(data_tratado_float)
print('------------???????-------------------')

#data_tratado_float.info()
print('--------------!!!-----------------')

#data_frame_tratado.info()
print('--------------kkk-----------------')

new_data.info()

saida = pd.DataFrame(data = data_frame_tratado)
print('--------------kkk-----------------')

print(saida)

saida.to_excel('eagora.xlsx')


percen_newdata = (new_data.isnull().sum() / len(new_data['Hematocrit'])) *100

percen = (data_frame_tratado.isnull().sum() / len(data_frame_tratado['Hematocrit'])) *100

print('-------------------------------')
null = new_data.isnull().sum()
print(percen)
print('-------------------------------')
print(percen_newdata)
print('-------------------------------')
