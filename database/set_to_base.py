"""code for transfering the dataframe to a database"""
import sqlite3
import pandas as pd

"""
- strain name
- type
- thc content
- cbd content
- 1 description
- medical effects
- flavor
- effects
"""


needed_columns = ['id', 'strain', 'effect', 'medical_effect_plain', 'flavor', 'Type', 'THC_Percent',
                  'CBD', 'Description1']

df1 = pd.read_csv('C:/Users/PhatDeluxe/buildweek_unit3/Machine-learning/database/no_nan_data.csv')

df = pd.DataFrame()

for item in needed_columns:
    df[item] = df1[item]

sl_conn = sqlite3.connect('med_cabinet3.sqlite3')
sl_curs = sl_conn.cursor()

model_id = 1

df.to_sql('strain_info', con=sl_conn)

sl_curs.close()
sl_conn.commit()