import pandas as pd, time, re
df = pd.read_csv('pokemon_data.csv')

i=0
for df in pd.read_csv('pokemon_data.csv', chunksize=100):
    df['count']=1
    if i==0:
        new_df = pd.DataFrame()
    i+=1
    print ('CHUNK #'+ str(i))
    results = df.groupby(['Type 1']).count()['Name']
    new_df = pd.concat([new_df, results])
##    print   (new_df)
##new_df['0']=int(new_df['0'])

print(new_df.groupby(level=0).sum())
new_df.to_excel('new.xlsx')
