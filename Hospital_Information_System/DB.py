import sqlite3

def createDatabaseAndTables():
    try:
        sqliteConnection = sqlite3.connect("Hospital_Database.db")

        create_hospitals_table_query = ''' CREATE TABLE IF NOT EXISTS Hospitals (
                                            Hospital_id INTEGER NOT NULL PRIMARY KEY,
                                            Hospital_name TEXT NOT NULL,
                                            Bed_count INTEGER
                                            );
                                        '''
        
        create_doctors_table_query = ''' CREATE TABLE IF NOT EXISTS Hospitals (
                                            Doctor_id INTEGER NOT NULL PRIMARY KEY,
                                            Doctor_name TEXT NOT NULL,
                                            Hospital_id INTEGER NOT NULL,
                                            Joining_date TEXT NOT NULL,
                                            Speciality TEXT NOT NULL,
                                            Salary INTEGER NOT NULL,
                                            Experience INTEGER,
                                            FOREIGN KEY (Hospital_id) REFERENCES Hospitals (Hospital_id)
                                            );
                                        '''

        cursor = sqliteConnection.cursor()
        print("Connected to sqlite!")

        cursor.execute(create_hospitals_table_query)
        cursor.execute(create_doctors_table_query)
        sqliteConnection.commit()

        print("Tables Created successfully!")
        
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to create table.", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Sqlite connection is closed")

createDatabaseAndTables()