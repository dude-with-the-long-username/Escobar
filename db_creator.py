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
        address TEXT,
        phone_number TEXT CHECK (LENGTH(phone_number) = 10) 
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT CHECK (LENGTH(phone_number) = 10) 
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
        date TEXT,
        FOREIGN KEY (pat_id) REFERENCES patients(id),
        FOREIGN KEY (drug_id) REFERENCES drugs(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pat_id INTEGER,
        date TEXT,
        drug_id INTEGER,
        quantity INTEGER,
        price INTEGER,
        FOREIGN KEY (pat_id) REFERENCES patients(id),
        FOREIGN KEY (drug_id) REFERENCES drugs(id)
    )
''')

connection.close()

