"""
Script to list the privileges of MySQL users user_0d_1 and user_0d_2 on the localhost server.
"""

import mysql.connector

def list_user_privileges(username):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_mysql_username",
            password="your_mysql_password",
            database="mysql"  # The system database where user privileges are stored
        )

        cursor = connection.cursor()

        # Query to list privileges for a specific user
        query = f"SHOW GRANTS FOR '{username}'@'localhost';"
        cursor.execute(query)

        # Fetch and print the results
        results = cursor.fetchall()
        for result in results:
            print(result[0])

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# List privileges for user_0d_1
list_user_privileges('user_0d_1')

# List privileges for user_0d_2
list_user_privileges('user_0d_2')

