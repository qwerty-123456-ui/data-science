import re
import pandas as pd 
df=pd.read_csv('pokemon_data.csv')
# df=pd.read_excel(pokemon_data.xlsx')
#df=pd.read_csv('pokemon_data.txt',delimiter='\t')
#print(df.xlsx.head(3))
# print(df.head(3))
#print(df.head())#default 5
# print(df.tail(3))
#read headers
# print(df.columns)
# read each column
# print(df['Name'][0:5])
# print(df.Name)
#multiple columns
# print(df[['Name','Type 1','HP']])
#read each row
# print(df.head(4))
# print(df.iloc[1])
# print(df.iloc[1:4])
#read a specific location[r,c]
# print(df.iloc[2,1])
# for index,row in df.iterrows():
#     print(index,row['Name'])
# print(df.loc[df['Type 1']=='Fire'])
# print(df.describe())
# print(df.sort_values('Name'))
# print(df.sort_values('Name',ascending=False))
# print(df.sort_values(['Type 1','HP'],ascending=[1,0]))
# df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
# print(df.head(5))
# df=df.drop(columns=['Total'])
# print(df.head(5))

# df['Total']=df.iloc[:,4:10].sum(axis=1)
# cols=list(df.columns)
# df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.head(5))
#saving our data
# df.to_csv('modified.csv',index=False)
# df.to_excel('modified.xlsx',index=False)
# df.to_csv('modified.txt',index=False,sep='\t')
#filtering data
# print(df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')])
# print(df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison') & (df['HP']>70)])
# new_df=df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison') & (df['HP']>70)]
# print(new_df)

# new_df.reset_index(drop=True,inplace=True)
# print(new_df)
# new_df.to_csv('filtered.csv')
# print(df.loc[~df['Name'].str.contains('Mega')])
# print(df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)])
# to ignore case
# print(df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)])
# print(df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)])
#conditional changes
# df.loc[df['Type 1']=='Fire','Type 1']='Flamer'
# df.loc[df['Type 1']=='Flamer','Type 1']='Fire'
# df.loc[df['Type 1']=='Fire','Legendary']=True
# print(df)
# df=pd.read_csv('modified.csv')
# print(df)
df['Total']=df.iloc[:,4:10].sum(axis=1)
cols=list(df.columns)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(5))
print(df)
# df.loc[df['Total']>500,['Generation','Legendary']]='Test Value'
# print(df)
# df.loc[df['Total']>500,['Generation','Legendary']]=['Test Value','fuck']
# print(df)
#aggregrate statistics(groupby)
df.to_csv('modified.csv')
# print(df)
# print(df.groupby(['Type 1']).mean())
# print(df.groupby(['Type 1']).mean().sort_values('HP',ascending=False))
# print(df.groupby(['Type 1']).sum())
# print(df.groupby(['Type 1']).count())
# df['count']=1
# print(df)
# print(df.groupby(['Type 1']).count()['count'])
# print(df.groupby(['Type 1','Type 2']).count()['count'])
#working with large amt o data
new_df=pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv',chunksize=5):
    # print("chunk ")
    # print(df)
    results=df.groupby(['Type 1']).count()

new_df=pd.concat([new_df,results])