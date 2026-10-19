import sqlite3

def insert_many_records(table, records):
    try:
        sqliteConnection = sqlite3.connect("Hospital_Database.db")
        cursor = sqliteConnection.cursor()
        print("Connected with database successfully!")

        if table == "Hospitals":
            insert_query = ''' INSERT INTO Hospitals (Hospital_id, Hospital_name, Bed_count)
                                VALUES (?, ?, ?)
                            '''

        cursor.executemany(insert_query, records)
        sqliteConnection.commit()
        print(f"{cursor.rowcount} inserted in {table} table successfully!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert records in table!", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Sqlite connection is closed!")

def insert_one_record(table, record):
    try:
        sqliteConnection = sqlite3.connect("Hospital_Database.db")
        cursor = sqliteConnection.cursor()
        print("Connected with database successfully!")

        if table == "Hospitals":
            insert_query = ''' INSERT INTO Hospitals (Hospital_id, Hospital_name, Bed_count)
                                VALUES (?, ?, ?)
                            '''

        cursor.execute(insert_query, record)
        sqliteConnection.commit()
        print(f"{cursor.rowcount} inserted in {table} table successfully!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert records in table!", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Sqlite connection is closed!")

def list_all_records(table):
    try:
        sqliteConnection = sqlite3.connect("Hospital_Database.db")
        cursor = sqliteConnection.cursor()
        print("Connected to database successfully!")

        Query = f'SELECT * FROM {table}'

        cursor.execute(Query)
        records = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to fetch records", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("SQLite connection is closed!")
            return records