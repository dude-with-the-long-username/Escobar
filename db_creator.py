import sqlite3
import os

# delete database file if it exists
if os.path.exists("pharmacy.sqlite"):
    os.remove("pharmacy.sqlite")
if os.path.exists("pharmacy.db"):
    os.remove("pharmacy.db")

connection = sqlite3.connect("pharmacy.sqlite")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        addressline1 TEXT,
        addressline2 TEXT,
        city TEXT,
        phone_number TEXT NOT NULL CHECK (LENGTH(phone_number) = 10) 
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL CHECK (LENGTH(phone_number) = 10) 
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS drugs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price INTEGER,
        quantity INTEGER,
        manufacturer_id INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS manufacturer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT CHECK (LENGTH(phone_number) = 10)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pat_id INTEGER,
        drug_id INTEGER,
        dosage INTEGER,
        date TEXT
    )
''')

connection.close()

