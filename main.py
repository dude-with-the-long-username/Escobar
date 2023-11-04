import sqlite3

db = sqlite3.connect('pharmacy.sqlite')
cursor = db.cursor()

print('\nPharmacy Management System\n\n')

while(1):
    print('''
    what would you like to manage?
    1. patients
    2. doctors
    3. users
    4. drugs
    5. drug manufacturers
    6. prescriptions
    7. Exit

    Enter your choice:''')

    main_menu_choice = int(input())
    if main_menu_choice == 1:
        while(1):
            print(' What would you like to do?')
            print(' 1. Add patient')
            print(' 2. Update patient')
            print(' 3. Delete patient')
            print(' 4. View patient details')
            print(' 5. Go to previous menu')
            print(' \nEnter your choice:')

            pat_menu_choice = int(input())
            if pat_menu_choice == 1:
                print('\n   Enter patient name:')
                pat_name = str(input())
                print('\n   Enter address:')
                pat_addr = str(input())
                print('\n   Enter phone number:')
                pat_phone = str(input())
                cursor.execute('''INSERT INTO 
                                        patients(name,address,phone_number)
                                    VALUES(?,?,?)''', (pat_name,pat_addr,pat_phone))
                db.commit()
                print("patient successfully added!\n")
            elif pat_menu_choice == 4:
                print('\n   The patients are:\n')
                cursor.execute('''SELECT * FROM patients''')
                print('\tid\tname\taddress\t\tphone_number')
                for row in cursor:
                    print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
                print('\n\n')
            elif pat_menu_choice == 5:
                break
            else:
                print('Enter a valid choice!\n')
    elif main_menu_choice == 7:
        break
    else:
        print('Enter a valid choice!\n')

db.close()