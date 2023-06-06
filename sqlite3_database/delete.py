def delete():
    import sqlite3
    #DELETE
    conn = sqlite3.connect('D.db')
    cursor = conn.cursor()
    print("Opened database successfully")
    #刪除name='星野好造'
    T=input('TABLE:')
    d=input('delete name:')
    cursor.execute(f"DELETE from {T} where name = '{d}';")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes,'\n')
    cursor = conn.execute(f"SELECT id, name, car, color  from {T}")

    for row in cursor:
        print(row)
    if conn.total_changes>0:
        conn.commit()#執行sql語法
        print("Operation done successfully")
        cursor.close()#關閉游標
        conn.close()#關閉連結
        print( "Operation done successfully")
        conn.close()
    else:
        print('error')
        
if __name__=='__main__':
    delete()