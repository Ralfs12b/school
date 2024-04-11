def display_vakances():
      cursor = connection.cursor()
      query = f'SELECT * FROM {table_name}'
      cursor.execute(query)
      rows = cursor.fetchall()
      for row in rows:
            print(row)
