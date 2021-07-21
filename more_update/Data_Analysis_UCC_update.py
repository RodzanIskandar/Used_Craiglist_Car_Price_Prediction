import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('vehicles.csv')

# Data Cleaning
df.info()
df.isnull().sum()
df_sample = df.sample(10)
drop_columns = ['id', 'url', 'region_url', 'VIN', 'image_url', 'county']
df.drop(drop_columns, axis=1, inplace=True)

df.isnull().mean()*100

#price threshold 100 < price < 50000
df = df[(df['price'] >= 100) & (df['price'] <= 50000)]

#NAN data
fill_med_columns = ['year', 'odometer']
for col in fill_med_columns:
    median = df[col].median()
    df[col].fillna(median, inplace=True)
    
nan_columns = [column for column in df.columns if df[column].isnull().sum() > 1]    
unique_count_columns = [column for column in nan_columns if column not in ['description'] + ['lat'] + ['long']]
for col in unique_count_columns:
    unique = df[col].unique()
    print(col +': {}'.format(unique))

for col in unique_count_columns:
    df[col].fillna('other', inplace=True)
    
df['description'].fillna('not define', inplace=True)

# Data Analysis
df.info()
num_columns = [column for column in df.columns if df[column].dtypes != 'O']
for col in num_columns:
    fig, axs = plt.subplots(3,2)
    i = 0 
    for col in num_columns:
        plt.subplot(3,2, i+1)
        sns.histplot(data=df, x=col)
        i += 1