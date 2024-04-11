def display_vakances(cursor, ...):
    query = f'SELECT * FROM {...}'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
      print(row)