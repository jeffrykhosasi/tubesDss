import pandas as pd
import pickle

df = pd.read_csv("../bank/bank (copy).csv")
number_customer = df.shape[0]
annual_balance = df['balance'].mean(axis=0)
cust_joined = df[df['y'] == 'yes'].shape[0]
percent_cust_joined = round((cust_joined/number_customer)*100, 2)
map_month = {'jan': df[df['y'] == 'yes']['month'].value_counts()['jan'],
             'feb': df[df['y'] == 'yes']['month'].value_counts()['feb'],
             'mar': df[df['y'] == 'yes']['month'].value_counts()['mar'],
             'apr': df[df['y'] == 'yes']['month'].value_counts()['apr'],
             'may': df[df['y'] == 'yes']['month'].value_counts()['may'],
             'jun': df[df['y'] == 'yes']['month'].value_counts()['jun'],
             'jul': df[df['y'] == 'yes']['month'].value_counts()['jul'],
             'aug': df[df['y'] == 'yes']['month'].value_counts()['aug'],
             'sep': df[df['y'] == 'yes']['month'].value_counts()['sep'],
             'oct': df[df['y'] == 'yes']['month'].value_counts()['oct'],
             'nov': df[df['y'] == 'yes']['month'].value_counts()['nov'],
             'dec': df[df['y'] == 'yes']['month'].value_counts()['dec']}
last_camp = df['poutcome'].value_counts()

model_train = pickle.load(open('lgb.pkl', 'rb'))
