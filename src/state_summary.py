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

    ### 1. Type of unit ###
    ### a. the number of units weighted and unweighted ###
    print("\nthe number of units weighted and unweighted\n")
    cursor.execute('''SELECT st, sum(units_unwght),sum(units_wght)
                    FROM demographics.`database sel_typ`
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "Total Units Unweighted", "Total Units Weighted"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")
     
    ### b.information on the main ingredients of the demographic multipliers ###
    ### total number of people and number of people by age category ###
    print("\nInformation on the main ingredients of the demographic multipliers, total number of people and number of people by age category\n")
    cursor.execute('''SELECT st, sum(people),sum(age0_4),sum(age5_17),sum(age18_34),sum(age35_44),sum(age45_54),sum(age55_64),sum(age65_74),sum(age75pls)
                    FROM demographics.`database sel_typ` 
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "Total Number of People", "age0_4","age5_17","age18_34","age35_44","age45_54","age55_64","age65_74","age75pls"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")

    ### SAC, PSC ###
    print("\nInformation on the main ingredients of the demographic multipliers, SAC, PSC\n")
    cursor.execute('''SELECT st,sum(sacsch),sum(sack_5),sum(sac6_8),sum(sac9_12),sum(pscsch),sum(psck_5),sum(psc6_8),sum(psc9_12)
                    FROM demographics.`database sel_typ` 
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "sacsch", "sack_5","sac6_8","sac9_12","pscsch","psck_5","psc6_8","psc9_12"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")

    ### the demographic multipliers  ###
    ### total number of people and number of people by age category ###
    print("\nthe demographic multipliers, total number of people and number of people by age category\n")
    cursor.execute('''SELECT st, sum(dm_ppl),sum(dm_age04),sum(dm_age5_17),sum(dm_age18_34),sum(dm_age35_44),sum(dm_age45_54),sum(dm_age55_64),sum(dm_age65_74),sum(dm_age75pls)
                    FROM demographics.`database sel_typ` 
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "Total Number of People", "dm_age04","dm_age5_17","dm_age18_34","dm_age35_44","dm_age45_54","dm_age55_64","dm_age65_74","dm_age75pls"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")

    ### SAC, PSC ###
    print("\nthe demographic multipliers, SAC, PSC\n")
    cursor.execute('''SELECT st,sum(dm_sac),sum(dm_sack_5),sum(dm_sac6_8),sum(dm_sac9_12),sum(dm_psc),sum(dm_psck_5),sum(dm_psc6_8),sum(dm_psc9_12)
                    FROM demographics.`database sel_typ`
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "dm_sac", "dm_sack_5","dm_sac6_8","dm_sac9_12","dm_psc","dm_psck_5","dm_psc6_8","dm_psc9_12"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")
    
     ### SAC, PSC ###
    print("\nthe demographic multipliers, SAC, PSC\n")
    cursor.execute('''SELECT st,sum(value_hs_adj),sum(value_hs_p33),sum(value_hs_p67)
                    FROM demographics.`database sel_typ` 
                    GROUP BY st;''')
    data=cursor.fetchall()
    
    if data:
        headers = ["st", "value_hs_adj", "value_hs_p33","value_hs_p67"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("No data found for the specified state.")

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL server: {e}')
finally:
    if conn is not None:
        conn.close()