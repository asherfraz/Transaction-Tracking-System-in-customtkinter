import customtkinter
from components.MessageBox import exit_application, show_thanks
import sqlite3
import os
import datetime


class DatabaseHandler:

    def __init__(self):
        super().__init__()

    def DatabaseConnect(DB_PATH):
        try:
            return sqlite3.connect(DB_PATH)
        except sqlite3.Error as error:
            print(f"Database Connecting Error: {error}\n")
            return None

    def createTransactionTable(dbConnection):
        print("Databse: createTransactionTable")
        # Create a cursor object to interact with the database
        dbCusor = dbConnection.cursor()
        try:
            # Define the SQL query to create the table
            Transactions_table_query = """
                CREATE TABLE IF NOT EXISTS Transactions (
                    transID INTEGER PRIMARY KEY AUTOINCREMENT,
                    productName VARCHAR(255),
                    productPrice INTEGER,
                    productQuantity INTEGER,
                    DateTime VARCHAR(255)
                )
            """
            # Try to execute the create table query
            dbCusor.execute(Transactions_table_query)

            # Commit the changes to the database
            dbConnection.commit()
            print("Database: Transactions Table Created Successfully!")

        except sqlite3.OperationalError as e:
            # Handle the case where the table already exists
            print(f"Table 'Transactions' already exists. : {e}")

    # def insertTransactionTable(dbConnection, productData):
    def insertTransactionTable(dbConnection, productData):
        print("Databse: insertTransactionTable")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Insert data into the table
            insert_data_query = """
                INSERT INTO Transactions (productName, productPrice, productQuantity,DateTime)
                VALUES (?, ?, ?, ?) 
            """
            dbCusor.execute(insert_data_query, productData)
            dbConnection.commit()
            print("Database: inserted successfully.")

            DatabaseHandler.viewTransactionTable(dbConnection)
            return True

        except sqlite3.OperationalError as e:
            print(f"Insert into Transtions Table Failed. : {e}")
            return False

    def viewTransactionTable(dbConnection):
        print("Databse: viewTransactionTable")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Print all the rows
            # print("(ID, Name, price, quantity, DateTime)")
            # for row in dbCusor.execute("SELECT * FROM Transactions"):
            #     print(row)
            dbCusor.execute("SELECT * FROM Transactions")
            rows = dbCusor.fetchall()
            return rows

        except sqlite3.OperationalError as e:
            print(f"viewTransactionTable Failed : {e}")
            return False

    def updateTransactionbyID(dbConnection, datalist):
        print("Databse: updateTransactionbyID")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Print all the rows
            # print("(ID, Name, price, quantity, DateTime)")
            dbCusor.execute(
                f"""UPDATE Transactions SET productName = '{datalist[1]}', productPrice = {datalist[2]}, productQuantity = {datalist[3]}, DateTime = '{datalist[4]}' WHERE transID = {datalist[0]}"""
            )
            #     (
            #         new_product_name,
            #         new_product_price,
            #         new_product_quantity,
            #         new_datetime,
            #         trans_id_to_update,
            #     ),
            # )
            # Commit the transaction
            dbConnection.commit()
            print("Database: Updated successfully.")
            return True

        except sqlite3.OperationalError as e:
            print(f"updateTransactionbyID Failed : {e}")
            return None

    def viewTransactionbyID(dbConnection, Id):
        print("Databse: viewTransactionbyID")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Print all the rows
            # print("(ID, Name, price, quantity, DateTime)")
            dbCusor.execute(f"SELECT * FROM Transactions where transID={Id}")
            row = dbCusor.fetchall()
            print(row)
            return row

        except sqlite3.OperationalError as e:
            print(f"viewTransactionbyID Failed : {e}")
            return None

    def viewTransactionbyName(dbConnection, name):
        print("Databse: viewTransactionbyName")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Print all the rows
            # print("(ID, Name, price, quantity, DateTime)")
            dbCusor.execute(f"SELECT * FROM Transactions where productName='{name}'")
            row = dbCusor.fetchall()
            print(row)
            return row

        except sqlite3.OperationalError as e:
            print(f"viewTransactionbyName Failed : {e}")
            return None

    def deleteTransactionbyID(dbConnection, Id):
        print("Databse: deleteTransactionbyID")
        try:
            # Create a cursor object to interact with the database
            dbCusor = dbConnection.cursor()
            # Print all the rows
            dbCusor.execute(f"DELETE FROM Transactions WHERE transId={Id}")
            dbConnection.commit()
            print("Record Deleted!")
            return True

        except sqlite3.OperationalError as e:
            print(f"viewTransactionbyID Failed. : {e}")
            return False
