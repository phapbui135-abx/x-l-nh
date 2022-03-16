import pyodbc



def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("Select * from person")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute("insert into person(ID,name) values(?,?);",('12','Toan'))
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute('update person set name = ? where id = ?;',('Nam','8'))
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute('delete from person where id = ?;',('5'))
    conn.commit()
    read(conn)

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=PHAPBUI135\SQLEXPRESS;"
    "Database=people;"
    "Trusted_Connection=yes;"
)
read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()