def delete_profile(vārds):
    sql = "DELETE FROM ... WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    db.commit()
    if cursor.rowcount == 0:
        print("Jūsu profils netika atrasts")
    else:
        print("Jūsu profils tika izdzēst")