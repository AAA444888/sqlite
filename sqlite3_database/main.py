import os
import create
import insert
import query
import update
import delete
import download

while True:
    try:
        choice=input('(0)create, (1)insert, (2)query, (3)update, (4)delete, (5)download, (6)exit:')
        if choice == '0':
            create.create_()
        elif choice == '1':
            insert.insert()
        elif choice == '2':
            query.query()
        elif choice == '3':
            update.update()
        elif choice == '4':
            delete.delete()
        elif choice == '5':
            download.download()
        elif choice == '6':
            break
    except IOError as e:
        print('e')
        break