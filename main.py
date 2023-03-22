import pandas as pd
import numpy as np 

pd.options.display.max_rows = 99
# pd.options.display.max_columns = 9

dataframe = pd.read_excel('dataset.xlsx')

# print(dataframe.head(10))


#print(dataframe.columns)



# for t in test:
#     if (t != True ):
#         print(dataframe['Hematocrit'])
# k = 0

def dt_results(dataframe,columns=50): 
    k = 0
    for i in range(columns):
        test = pd.isnull(dataframe[dataframe.columns[i]])
        for j in range(len(dataframe[dataframe.columns[i]])):
            if test[j] != True:
                valor = dataframe[dataframe.columns[i]].values[j]
                # print(valor)
                k += 1
    return k



def drop_columns(data, n,m =111):
    
    temp = data
    for i in range(n,m):
    
        new_data = temp.drop([temp.columns[i]], axis=1)
        temp =  new_data
        print(new_data.head(-5))
        m -=1 
        print(m)
        

    return new_data
    
    
    


# dt_full_valores = dataframe.dropna(how='all')
# print(dt_full_valores.head())

# kn = dt_results(dataframe,111)
#print(kn)

# m = dt_results(dt_full_valores,111)
# print(m)

dt_full_valores = drop_columns(dataframe,60)
print(dt_full_valores)

#dt_full_valores.to_excel('sem_valores_NaN2.xlsx')
 

    

