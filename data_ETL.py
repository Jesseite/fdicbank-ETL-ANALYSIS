import psycopg2
import os
from psycopg2 import sql

#PostgreSQL connection information
conn = None
try: 
    conn=psycopg2.connect(
        database = os.environ.get('postgres_database')
        ,user = os.environ.get('postgres_user')
        ,password = os.environ.get('postgres_password')
        ,host = os.environ.get('postgres_host')
        ,port = os.environ.get('postgres_port')  
    )

    conn.autocommit = True
    cursor = conn.cursor()

    #Create a table
    create_sql_table = '''CREATE TABLE IF NOT EXISTS public.fdic_bank_failures(
                        bank_id INT PRIMARY KEY
                        ,bank_name VARCHAR(120)
                        ,city VARCHAR(120)
                        ,state VARCHAR(120)
                        ,cert INT
                        ,acquired_by VARCHAR(120)
                        ,closed_date DATE
                        ,fund INT)'''

    cursor.execute(create_sql_table)

    #Copy data from banklistv2.csv
    copy_csv = '''COPY fdic_bank_failures(
                             bank_id
                            ,bank_name
                            ,city
                            ,state
                            ,cert
                            ,acquired_by
                            ,closed_date
                            ,fund)
    FROM 'banklistv2.csv' WITH CSV HEADER DELIMITER '|';'''
    
    with open(os.environ.get('csv_transform'), 'r') as f:
        next(f)  # Skip the header row.
        cursor.copy_from(file=f, table='fdic_bank_failures', sep='|', null="")

    #Check if data is loaded
    check_table = '''SELECT * FROM public.fdic_bank_failures;'''

    cursor.execute(check_table)
    for i in cursor.fetchall():
        print(i)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn is not None:
        conn.close()