"""code to retrieve data from the database"""

import sqlite3


def strain_info(id_list, distance_list):
    """takes in the list of two arrays returned from the model
    and returns all the information about the strains
    in a json format"""

    #connectiong to the database
    sl_conn = sqlite3.connect('med_cabinet3.sqlite3')
    sl_curs = sl_conn.cursor()


    #initalizing the list to be returned
    return_list = []


    #the columns that will be retrieved from the database
    needed_columns = ['strain', 'effect', 'medical_effect_plain',
                      'flavor', 'Type', 'THC_Percent',
                      'CBD', 'Description1']


    #Creating a list then adding key-value-pairs to said list
    # ends by appending the key-value-pair list to another list as a key-value-pair 
    for i in range(0, 5):
        strain_list = {}
        strain_list['Recommendation'] = i + 1
        for item in needed_columns:
            request = f'SELECT {item} FROM strain_info WHERE id = {id_list[i]};'
            value = str(sl_curs.execute(request).fetchall())
            #For some reason the SQL query returns something 
            # formatted like (['<strain-name>,]) so this is 
            # to remove all the useless characters
            value = value.replace(')', '')
            value = value.replace('[', '')
            value = value.replace(']', '')
            value = value.replace('(', '')
            value = value.replace(',', '')
            value = value.replace("'", '')
            strain_list[item] = value
        strain_list['Score'] = distance_list[i]
        return_list.append(strain_list)
    sl_curs.close()
    return return_list
