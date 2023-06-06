def download():
    import sqlite3
    conn = sqlite3.connect("D.db")#連結資料庫
    cursor = conn.cursor()#啟用游標
    print("Opened database successfully")
    import pandas as pd
    #匯入至pandas
    T=input('TABLE:')
    cursor = cursor.execute(f"SELECT * from {T}")
    df = pd.DataFrame(cursor, columns= ["id", "name", "car", "color"])
    print(df,'\n')
    #匯入至 .xlsx
    n=input('excel name:')
    if n=="":
        df.to_excel("drift_home.xlsx", index = False)
    else:
        df.to_excel(f"{n}.xlsx", index = False)
    print("Operation done successfully")
    cursor.close()#關閉游標
    conn.close()#關閉連結

if __name__=='__main__':
    download()