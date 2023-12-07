def modify_profile(vards):
    sql = "SELECT * FROM book WHERE name = %s"
    value = (vards,)
    cursor.execute(sql, value)
    profile = cursor.fetchone()
    if profile is None:
        print("Profils neeksistē")
    else:
        while True:
            print("\nPress the option you want to edit: ")
            print("1. Vārds")
            print("2. Profesija")
            print("3. Novads")
            print("4. Izglītība")
            print("5. Preference")
            print("6. ATPAKAĻ")
            print()
            ch = int(input("IZVĒLIES no 1 līdz 6: "))
            if ch == 1:
                new_name = input("Enter jaunu vārdu: ")
                sql = "UPDATE book SET vārds = %s WHERE vārds = %s"
                values = (new_name, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Jūsu profils tika atjaunots")
            elif ch == 2:
                new_profession = input("Enter jauno profesiju: ")
                sql = "UPDATE book SET profesija = %s WHERE vārds = %s"
                values = (new_profession, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Jūsu profils tika atjaunots")
            elif ch == 3:
                new_novads = input("Enter jūsu jauno novadu: ")
                sql = "UPDATE book SET novads = %s WHERE vārds = %s"
                values = (new_novads, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Jūsu profils tika atjaunots")
            elif ch == 4:
                new_izglitiba = input("Enter jūsu tagadējā izglītība: ")
                sql = "UPDATE book SET izglītība = %s WHERE vārds = %s"
                values = (new_izglitiba, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Jūsu profils tika atjaunots")
            elif ch == 5:
                new_preference = input("Enter preferenci: ")
                sql = "UPDATE book SET preference = %s WHERE vārds = %s"
                values = (new_preference, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Jūsu profils tika atjaunots")
            elif ch == 6:
                break
            else:
                print("Nepareiza izvēle no 1 līdz 6 !!!\n")
