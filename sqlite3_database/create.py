def create_():
    import sqlite3
    #drop table 
    conn = sqlite3.connect('D.db')#連結資料庫，如果沒有則會建立
    print ("Opened database successfully")
    cursor = conn.cursor()#啟用游標
    cursor.execute("DROP TABLE  IF EXISTS  person;")#查看是否存在away
    cursor.execute("DROP TABLE  IF EXISTS  home;")#查看是否存在home
    cursor.execute('''CREATE TABLE IF NOT EXISTS person 
        (id INT PRIMARY KEY NOT NULL,
        name varchar(8) NOT NULL,
        car varchar(30) NOT NULL,
        color varchar(10) NOT NULL);''')
    print ("Table person created successfully")
    #設定home資料表
    cursor.execute('''CREATE TABLE IF NOT EXISTS home 
        (id INT PRIMARY KEY NOT NULL,
        name varchar(8) NOT NULL,
        car varchar(30) NOT NULL,
        color varchar(10) NOT NULL);''')
    print ("Table home created successfully")
    conn.commit()#執行sql語法，每次執行都要提交sql語法
    cursor.close()#每次執行都要關閉游標
    conn.close()#每次執行都要關閉連結

if __name__=='__main__':
    create_()