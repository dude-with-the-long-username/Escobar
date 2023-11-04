# contains common functions to use in program

import sqlite3
import datetime

db = sqlite3.connect('pharmacy.sqlite')
cursor = db.cursor()

def list_all_prescriptions():
    print('\n   List of all prescriptions:\n')
    cursor.execute('''
                        SELECT 
                            presc.id
                            , pat.name
                            , drug.name
                            , presc.dosage
                            , presc.date
                        FROM prescriptions presc
                            INNER JOIN patients pat
                                ON presc.pat_id = pat.id
                            INNER JOIN drugs drug
                                ON drug.id = presc.drug_id
                    ''')
    print('\t\tid\t\tpatient\t\tdrug\t\tdosage\t\tdate')
    for row in cursor:
        print(f'\t\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}')
    print('\n\n')



def list_prescriptions_by_pat_id(pat_id):
    print('\n   List of all prescriptions:\n')
    cursor.execute('''
                        SELECT 
                            presc.id
                            , pat.name
                            , drug.name
                            , presc.dosage
                            , presc.date
                        FROM prescriptions presc
                            INNER JOIN patients pat
                                ON presc.pat_id = pat.id
                            INNER JOIN drugs drug
                                ON drug.id = presc.drug_id
                        WHERE pat_id = ?
                    ''', (pat_id))
    print('\t\tid\t\tpatient\t\tdrug\t\tdosage\t\tdate')
    for row in cursor:
        print(f'\t\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}')
    print('\n\n')


def list_prescriptions_by_drug_id(drug_id):
    print('\n   List of all prescriptions:\n')
    cursor.execute('''
                        SELECT 
                            presc.id
                            , pat.name
                            , drug.name
                            , presc.dosage
                            , presc.date
                        FROM prescriptions presc
                            INNER JOIN patients pat
                                ON presc.pat_id = pat.id
                            INNER JOIN drugs drug
                                ON drug.id = presc.drug_id
                        WHERE drug_id = ?
                    ''', (drug_id))
    print('\t\tid\t\tpatient\t\tdrug\t\tdosage\t\tdate')
    for row in cursor:
        print(f'\t\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t\t{row[4]}')
    print('\n\n')