def insert():
#insert
    import sqlite3
    conn = sqlite3.connect("D.db")#連結資料庫
    cursor = conn.cursor()#啟用游標
    print("Opened database successfully")
    try:
        v0=input('TABLE:')
        v1=int(input('請輸入id:'))
        v2=input('請輸入姓名:')
        v3=input('請輸入汽車:')
        v4=input('請輸入顏色:')
        #匯入資料至away資料表
        cursor.execute(f"INSERT INTO {v0} (id,name,car,color) VALUES ({v1}, '{v2}', '{v3}', '{v4}' )")
        conn.commit()#執行sql語法
    except:
        print('error')
    print("Records created successfully")
    cursor.close()#關閉游標
    conn.close()#關閉連結

if __name__=='__main__':
    insert()