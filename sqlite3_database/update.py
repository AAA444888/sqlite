def update():
    import sqlite3
    #update
    conn = sqlite3.connect('D.db')
    cursor = conn.cursor()
    print("Opened database successfully")
    try:
        f=True
        T=input("TABLE:")
        s="UPDATE "+T+" set "
        id=int(input('請輸入要update id:'))
        name=input('update name:')
        car=input('update car:')
        color=input('update color:')
        if name!="":
            s+="name = '"+name+"'"
            f=False
        if car!="":
            if f==False:
                s+=", "
            s+="car = '"+car+"'"
            f=False
        if color!="":
            if f==False:
                s+=", "
            s+="color = '"+color+"'"
        cursor.execute(s+f" where id = {id} ")
        conn.commit()
        #顯示更新幾筆
        print("Total number of rows updated :", conn.total_changes)

        cursor = conn.execute(f"SELECT id, name, car, color  from {T}")
        for row in cursor:
            print("id = ", row[0])
            print("name = ", row[1])
            print("car = ", row[2])
            print("color = ", row[3], "\n")

        print( "Operation done successfully")
    except:
        print('error')
    cursor.close()
    conn.close()

if __name__=='__main__':
    update()