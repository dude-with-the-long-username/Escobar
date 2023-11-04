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
                print('What would you like to do?')
                print('1. Add patient')
                print('2. Update patient')
                print('3. Delete patient')
                print('4. View patient details')
                print('5. Go to previous menu')
                print('\nEnter your choice:')
        pat_menu_choice = int(input())
        if pat_menu_choice == 1:
            print('\nEnter patient name:')
            pat_name = str(input())
            print('\nEnter addressLine1:')
            pat_addr1 = str(input())
            print('\nEnter addressLine2:')
            pat_addr2 = str(input())
            print('\nEnter city:')
            pat_city = str(input())
            print('\nEnter phone number:')
            pat_phone = str(input())
            cursor.execute('''INSERT INTO patients(name,addressline1,addressline2,city,phone_number)
                                VALUES(?,?,?,?,?)''', (pat_name,pat_addr1,pat_addr2,pat_city,pat_phone))
            db.commit()
            print("patient successfully added!\n")
    else:
        print('Enter a valid choice!\n')

db.close()