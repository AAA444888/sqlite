import sqlite3
#drop table 
conn = sqlite3.connect('D.db')#連結資料庫，如果沒有則會建立
cursor = conn.cursor()#啟用游標
cursor.execute("DROP TABLE  IF EXISTS  away;")#查看是否存在away
cursor.execute("DROP TABLE  IF EXISTS  home;")#查看是否存在home
print ("D.db created successfully")
conn.commit()#執行sql語法，每次執行都要提交sql語法
cursor.close()#每次執行都要關閉游標
conn.close()#每次執行都要關閉連結