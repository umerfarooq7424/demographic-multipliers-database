import os
import mysql.connector
from tabulate import tabulate

config = {
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''), 
    'host': os.environ.get('DB_HOST', 'localhost'), 
    'database':'demographics' 
}
conn=None
# Establish the database connection
try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print('Connected to MySQL server')
    cursor = conn.cursor()

    state= (input('Enter State: ')).lower()
    #cursor.execute('SELECT unit_type, sum(units_unwght),sum(units_wght), st FROM demographics.`database sel_alltyp` GROUP BY st,unit_type;')
    cursor.execute('''SELECT unit_type, sum(units_unwght),sum(units_wght),avg(dm_age18_34)
                    FROM (SELECT st,unit_type,units_unwght,units_wght,dm_age18_34 FROM demographics.`database sel_alltyp` WHERE st=%s) as new_table
                    GROUP BY unit_type;''',(state,))
    data=cursor.fetchall()
    print(data)
    if data:
        headers = ["Unit Type", "Total Units Unweighted", "Total Units Weighted","dm_age18_34"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")

    unit_type_to_find = input('Enter Unit Type: ')
    filtered_data = [(unit_type, total_units_unweighted, total_units_weighted,dm_age18_34) 
                 for unit_type, total_units_unweighted, total_units_weighted,dm_age18_34 in data 
                 if unit_type.lower() == unit_type_to_find.lower()]
    print('State: ',state)
    print('unit type: ', unit_type_to_find)
    print('total units unweighted: ',filtered_data[0][1])
    print('total units weighted: ',filtered_data[0][2])

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL server: {e}')
finally:
    if conn is not None:
        conn.close()