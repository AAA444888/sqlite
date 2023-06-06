def query():
    f=False
    import sqlite3
    #search
    conn = sqlite3.connect("D.db")#連結資料庫
    cursor = conn.cursor()#啟用游標
    print("Opened database successfully")
    #搜尋所有away的欄位資料
    cursor = cursor.execute("SELECT * from away")
    for row in cursor:
        print(row)
    #搜尋所有home的欄位資料
    cursor = cursor.execute("SELECT * from home")
    #顯示
    for row in cursor:
        print(row)
    cursor = cursor.execute("SELECT * from person")
    for row in cursor:
        print(row)
    T=input('TABLE:')
    a=input('name:')
    cursor = cursor.execute(f"SELECT * from {T} where name= '{a}'")
    for row in cursor:
        print(row)
        f=True
    conn.commit()#執行sql語法
    if f==True:
        print("Operation done successfully")
    else:
        print('error')
    cursor.close()#關閉游標
    conn.close()#關閉連結

if __name__=='__main__':
    query()