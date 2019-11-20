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




# class strain:
#     def __init__(self, id, strain, effect, plain, flavor, type, thc, cbd, desc):
#         self.id = 

        



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

return_list = []

for item in needed_columns:
    request = f'SELECT {item} FROM strain_info WHERE id = {model_id};'
    value = str(sl_curs.execute(request).fetchall())
    value = value.replace(')', '')
    value = value.replace('[', '')
    value = value.replace(']', '')
    value = value.replace('(', '')
    value = value.replace(',', '')
    value = value.replace("'", '')
    feature = {item: value}
    return_list.append(feature)


print(return_list)


# strain_list = sl_curs.execute('SELECT * FROM var1;').fetchall()


# terpenes = '''
#     CREATE TABLE terpenes (
#         terp_id INT,
#         terpine_type VARCHAR(15),
#         percent_t FLOAT
#     );
# '''

# cannabinoids = '''
#     CREATE TABLE cannabinoids (
#         noid_id INT,
#         cannabanoid_type VARCHAR(20),
#         percent_c FLOAT
#     );
#     '''

# strains = '''
#     CREATE TABLE strains (
#         id INT PRIMARY KEY,
#         name VARCHAR(30),
#         effects VARCHAR(300),
#         medical_use VARCHAR(300),
#         flavor VARCHAR(300),
#         type VARCHAR(10),
#         description1 CHAR,
#         description2 CHAR
#     );
#     '''

# table_list = [terpenes, cannabinoids, strains]

# for unit in table_list:
#     sl_curs.execute(unit)

# # sl_curs.execute(strains)

# cb_loc = [('CBG', 53), ('CBC', 54),
#           ('CBD', 49), ('CBDA', 48),
#           ('CBN', 47), ('THC', 10), 
#           ('THCA', 45), ('THCV', 45), 
#           ('CBDV', 50)]

# #labs = 15

# terp_loc = [('Myrcene', 36), ('Eucalyptol', 24),
#             ('Trans-nerolido', 17), ('Camphene', 22),
#             ('Geraniol', 25), ('Pinene', 33),
#             ('Terpinolene', 30), ('Limonene', 39),
#             ('Linalool', 28), ('B-Caryophyllene', 35)]


# for strain in strain_list:
#     insert_strain = '''
#     INSERT INTO strains
#     (id, name, effects, medical_use, flavor, type)
#     VALUES ''' + str(strain[2:8]) + ';'
#     sl_curs.execute(insert_strain)

    # insert_more_strain = '''
    # INSERT INTO strains
    # (description1)
    # VALUES ''' + str(strain[11]) + ';'
    # sl_curs.execute(insert_more_strain)

# , description1, description2)

    # for a, b in cb_loc:
    #     insert_cb = '''
    #     INSERT INTO cannabinoids
    #     (noid_id, cannabanoid_type, percent_c)
    #     VALUES ''' + '(' + str(strain[1]) + ', "' + str(a) + '", ' + str(strain[b]) + ')' + ';'
    #     sl_curs.execute(insert_cb)

    # for a, b in terp_loc:
    #     insert_terp = '''
    #     INSERT INTO terpenes
    #     (terp_id, terpine_type, percent_t)
    #     VALUES ''' + '(' + str(strain[1]) + ', "' + str(a) + '", ' + str(strain[b]) + ')' + ';'
    #     sl_curs.execute(insert_terp)


sl_curs.close()
sl_conn.commit()

print('Success')

"""
Myrcene found 35
Eucalyptol found 23
Trans-nerolido found 16
Camphene found 21
Geraniol found 24
Pinene found 32
Terpinolene found  29
Limonene found 38
Linalool found 27
B-Caryophyllene found 34
"""

"""
CBG found 52
CBC found 53
CBD found 48
CBDA found 47
CBN found 46
THC found 9
THCA found 44
THCV found 45
CBDV found 49
"""

