import pandas as pd
df = pd.DataFrame({
    "Name":["Aman","Biju","Charlie","Diya"],
    "Age" : [25,30,35,40],
},index=['a','b','c','d'])

#using df.loc to access rows directly use df["Tag"] to access full columns
print(df.loc['a']) #to access specific row
print(df.loc['c','Age'])

#use iloc for positional indexing instead of using tag names
print(df['Age'])

#using Boolean indexing to filter the data
print(df[df['Age']<32])

# .at and .iat similar to loc and iloc but faster access time 
print(df.iat[1,1])

#HANDLING MISSSING DATA
#detecting mising values will print the entire dataframe with the boolean answer of isnull or is not null (complements of each other )
print(df.isnull())
print(df.notnull())
 
#fillna to replace the NaN values with some value
#nan rows/cols are converted to float64 
# if inplace is not used a new data frame with the changed value is created

# df.fillna(23)
# print(df.iat[3,1])

newDF = df.dropna()
print(newDF)

#interpolating the data fills the values by creating an estimate using the surrounding values (uses a linear graph ie average unless mentioned otherwise)
df.infer_objects()
df = df.interpolate()
print(df)

#showing duplicate rows
print(df.duplicated())
#removing/dropping
df = df.drop_duplicates()
print(df)

#renaming using manual tags
# df.rename(columns={"Name":"First Name"},inplace=True) 
df.rename(index={'a':'row1'},inplace=True)
print(df)

#renaming using dictionaries if not found then it will replace with NaN

# df['First Name'] = df['First Name'].map({1:'one',2:'two'})

df['Age']  = df['Age'].apply(lambda x:x*2)
print(df)

#string methods

df['Name'] = df['Name'].str.upper()
print(df)

#merging two data frames
df1 = pd.DataFrame({
    'key':['A','B'],'val':[0,1]
})

df2 = pd.DataFrame({
    'key':['B','C'],'val':[3,4]
})

result = pd.merge(df1,df2,on='key',how='outer')
print(result)

result = result.fillna(0)
print(result)

#concatenating dataframes

# new = pd.concat([df1, df2], axis=0)  # stack rows
new  = pd.concat([df1, df2], axis=1)  # join columns
print(new)

#grouping and aggregating

groupdf = pd.DataFrame({
    'animal':['dog','cat','cat','dog'],
    'weight' :[45,32,33,48]
},index=['a','b','c','d'])

grouped = groupdf.groupby('animal')
# print(grouped['weight'].mean())  #aggregated with mean

#DATA TRANSFORMATION METHODS 


result  = groupdf.pivot_table(values='weight',index = 'animal',aggfunc='sum')
print(result)

#reshaping data
result = df.melt(id_vars=['Name'],value_vars=["Age"])
print(result)

#sorting 
# stores the entire data frame again in the said sorted order

result = groupdf.sort_values('weight',ascending=True)
print(result)

#ranking if there are same values then takes averages ex:3rd and 4th are same then will mark both as 3+4 whole /2 (spearmans rank corelation types)
result= df['Rank'] = df['Age'].rank(ascending=True)
print(result)

#date time 
datedf = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'value': [100, 110, 105]
})

datedf['date'] = pd.to_datetime(datedf['date'])  # Converts string to datetime
print(datedf['date'])

#resampling  if ur upsampling then u can use forward fill backward fill or extrapolating etc to fil in the values
#for downsampling we can take the min max or mean or sum etc to fill the values 
date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D') #time series data frame

df = pd.DataFrame({
    'date': date_range,
    'sales': [100, 120, 130, 90, 110, 150, 160, 170, 180, 190]
})

df.set_index('date', inplace=True)

print("Original Daily Data:")
print(df)

monthly_avg = df.resample('H').mean()

print("\nMonthly Resampled (Mean Sales):")
print(monthly_avg)


#vectorization faster than running loops
groupdf['weight'] = groupdf['weight']*2 
print(groupdf)


#categorical data  uses less memory as there are limited tags so the data is stored
#order of categories can also be mentioned
groupdf['animal'] = groupdf['animal'].astype('category')

print(groupdf['animal'])
print(groupdf['animal'].cat.categories)
