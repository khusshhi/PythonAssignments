import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.tsv',skiprows=1, sep='\t')
print(df.head())
# for row in df:
#        print(row)