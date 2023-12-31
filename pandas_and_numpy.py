import numpy as np
import pandas as pd
array1=np.arange(1,20)
print(array1)
print(array1+array1)
print(np.exp(array1))
print(np.sqrt(array1))
print(np.log(array1))
print(np.max(array1))
print(np.min(array1))
print(np.argmax(array1))
print(np.argmin(array1))
print(np.square(array1))
print(np.std(array1))
print(np.var(array1))
np.mean(array1)
array=np.random.randn(3,4)
print(array)
print(np.round(array,decimals=2))
sports=np.array(['golf','cricket','football','cricket'])
print(np.unique(sports))
sports1=pd.Series([1,2,3,4],index=['cricket','football','basketball','golf'])
sports1['football']
sports2=pd.Series([11,2,3,4],index=['cricket','football','baseball','golf'])
print(sports1+sports2)
df1=pd.DataFrame(np.random.rand(8,5),index='A B C D E F G H '.split(),columns='Score1 Score2 Score3 Score4 Score5'.split())
print(df1)
print(df1['Score1'])
print(df1[["Score1","Score2","Score3"]])
df1['Score6']=df1['Score1']+df1['Score3']
print(df1)
df2={'ID':['100','200','300','400','500'],'Name':['A','B','C','D','E'],'Profit':[10,50,20,60,70]}
df=pd.DataFrame(df2)
print(df)
print(df["ID"])
df=df.drop("ID",axis=1)
print(df)
print(df.drop(3))
