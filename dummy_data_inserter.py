import sqlite3
import os


db = sqlite3.connect("pharmacy.sqlite")
cursor = db.cursor()

cursor.execute('''
    INSERT INTO patients(name,address,phone_number)
    VALUES
        ('peter', 'neverland', '9890989098')
        , ('Teddy', 'Mumabattan', '7890987890')
        , ('Rosell', 'London', '9234567890')
        , ('Anthony', 'Nevada', '9098909878');
''')
db.commit()


cursor.execute('''
    INSERT INTO drugs(name,price,quantity)
    VALUES
        ('paracetamol', 45, 78)
        , ('ibuprofen', 56, 90)
        , ('Amoxicillin', 34, 90)
        , ('Strepsils', 78, 100);
''')
db.commit()

cursor.execute('''
    INSERT INTO prescriptions(pat_id,drug_id,dosage,date)
    VALUES
        (1, 1, 4, '2023-05-05')
        , (2, 3, 3, '2023-05-07')
        , (1, 2, 5, '2023-07-05')
        , (2, 4, 3, '2023-10-05')
        , (3, 4, 2, '2023-10-01');
''')
db.commit()

db.close()
