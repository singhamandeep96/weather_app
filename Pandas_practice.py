import pandas as pd

# data=[1,2,3,4,5]
# series=pd.Series(data)
# print("Series \n:", series)
# print(type(series))


# data={'a':1, 'b':2, 'c':3}
# series_dict=pd.Series(data)
# print(series_dict)

# data=[10,20,30]
# index=['a','b','c']
# a=pd.Series(data,index=index)
# print(a)

# data2={
#     'Name': ['Aman', 'Akash','Krish' ],
#     'Age':  [28,30,45],
#     'City': ['Delhi', 'Delhi', 'Bengalore']
# }

# df=pd.DataFrame(data2)
# print(df)
# print(type(df))


# data=[
#     {'Name':'Aman', 'Age': 28, 'City':'Delhi'},
#     {'Name': 'Akash','Age':30,'City': 'Delhi'},
#     {'Name': 'Krish', 'Age':45, 'City':'Bangalore'}
# ]

# df=pd.DataFrame(data)
# print(df)
# print(type(df))

# print(df['Name'])

# print(df.loc[0])

# print(df.iloc[0])

# print(df.at[2,'Age'])
# print(df.at[2,'Name'])
# print(df.iat[2,2])

# df['Salary']=[50000, 60000,70000 ]
# print(df)

# df.drop('Salary', axis=1, inplace=True)
# print(df)

# df['Age']=df['Age']+1

# df.drop(0, inplace=True)
# print(df)

df1=pd.DataFrame({'Key': ['A','B','C'], 'Value1':[1,2,3]})
df2=pd.DataFrame({'Key': ['A','B','D'], 'Value1':[4,5,6]})

print(df1)
print(df2)

merge=pd.merge(df1,df2, on="Key",how="inner" )
print(merge)

merge2=pd.merge(df1,df2, on="Key",how="outer" )
print(merge2)

merge3=pd.merge(df1,df2, on="Key",how="left" )
print(merge3)

merge4=pd.merge(df1,df2, on="Key", how="right")

