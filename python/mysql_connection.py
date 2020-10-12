""" This is an example script describing how to connect to mysql server and execu query 
    inorder to connect to mysql server we need `mysql-connector` use `pip install mysql-connector`
"""
import mysql.connector
import argparse

parser = argparse.ArgumentParser(description='Mysql database connection information')
parser.add_argument('--u', type=str, help='Database username', required=True)
parser.add_argument('--p', type=str, help='Database password', required=True)
parser.add_argument('--d', type=str, help='Database name', required=True) 
parser.add_argument('--H', type=str, help='Database hostname', required=True)
args = parser.parse_args()

#user inputs
username = args.u
password = args.p
database = args.d
host = args.H



def connect_to_mysql(host, database, username, password, authplugin='mysql_native_password'):
    """ connects to mysql server """
    try:
        print('Connecting to mysql server..........')
        connection = mysql.connector.connect(host=host, database=database, user=username, password=password, auth_plugin=authplugin)
        print("Connection established successfully..........")
        #TODO : Define your table here for testing
        connection.autocommit = False
        print('Setting auto commit to false for transaction..........')
        cursor = connection.cursor()
        query = """select * from {}""".format(table_name)
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Data fetched..........")
        row_headers = [x[0] for x in cursor.description]

        result = []
        for r in rows:
            result.append(dict(zip(row_headers, r)))

        print("result : {}".format(result))

        connection.commit()
    except mysql.connector.Error as e:
        connection.rollback()
        print("Exception occured..........")
    finally:
        if connection.is_connected():
            print("Connection is alive..........")
            cursor.close()
            print("Closing cursor..........")
            connection.close()
            print("Closing database connection..........")
if __name__ == "__main__":
    connect_to_mysql(host, database, username, password)

