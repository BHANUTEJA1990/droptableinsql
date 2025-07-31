import mysql.connector

connection = None # Initialize connection to None
cursorObj = None  # Initialize cursorObj to None

try:
    # establishing the connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysqlBhanuteja', # DOUBLE CHECK THIS PASSWORD AND USERNAME!
        database='bhanutejatools'
    )
    table_name = 'buyers'

    # Creating a cursor object 
    cursorObj = connection.cursor()

    # Check if table exists before dropping (optional but good practice)
    # This prevents an error if the table is already gone
    cursorObj.execute(f"SHOW TABLES LIKE '{table_name}'")
    if cursorObj.fetchone():
        drop_table_query = f"DROP TABLE {table_name}"
        cursorObj.execute(drop_table_query)
        print(f"Table '{table_name}' is dropped successfully.")
    else:
        print(f"Table '{table_name}' does not exist, nothing to drop.")

except mysql.connector.Error as err:
    # This block catches specific MySQL-related errors
    print(f"A database error occurred: {err}")
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Trouble logging in: Check your username and password.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_TABLE_ERROR:
        print(f"The table '{table_name}' might not exist or there's an issue with its name.")
    else:
        print("Unspecific MySQL error. Check connection details or table name.")
except Exception as e:
    # This catches any other unexpected Python errors
    print(f"An unexpected Python error occurred: {e}")
finally:
    # This block ensures that the cursor and connection are closed,
    # regardless of whether an error occurred or not.
    if cursorObj:
        cursorObj.close()
        print("Cursor closed.")
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
