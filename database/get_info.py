"""code to retrieve data from the database"""

import sqlite3


def strain_info(strain_id):
    """takes in the strain id and returns all the information about the strain"""
    sl_conn = sqlite3.connect('med_cabinet3.sqlite3')
    sl_curs = sl_conn.cursor()
    return_list = []

    needed_columns = ['strain', 'effect', 'medical_effect_plain',
                      'flavor', 'Type', 'THC_Percent',
                      'CBD', 'Description1']


    for item in needed_columns:
        request = f'SELECT {item} FROM strain_info WHERE id = {strain_id};'
        value = str(sl_curs.execute(request).fetchall())
        value = value.replace(')', '')
        value = value.replace('[', '')
        value = value.replace(']', '')
        value = value.replace('(', '')
        value = value.replace(',', '')
        value = value.replace("'", '')
        feature = {item: value}
        return_list.append(feature)

    sl_curs.close()
    return return_list