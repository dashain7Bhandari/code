
import sqlite3

def logInDetails():
    conn=sqlite3.connect("UserDetails.db")
    my_cursor=conn.cursor()

    # create_table='''CREATE TABLE IF NOT EXISTS Users (username VARCHAR(20), password VARCHAR(20))'''
    # my_cursor.execute(create_table)

    choice=int(input('Enter 1 to login and 0 to register\n'))

    if(choice==0):
        Username=input('Enter username\t')
        Password=input('Enter password\t')
        insert_script='''INSERT INTO Users VALUES ( "{Username}",
                "{Password}")'''.format(Username=Username,Password=Password)
        my_cursor.execute(insert_script)
        conn.commit()
        print('\nRegistration Successful\n')
        return 1
    
    else:
        select_cmd='''SELECT * FROM Users'''
        result=my_cursor.execute(select_cmd)
        count=0
        while(count!=1):
            Username=input('Enter username\t')
            Password=input('Enter password\t')
            for data in result: 
                
                if Username == data[0] and Password == data[1]:
                    count+=1
                    return 1
            
            if count==0:
                print('Your username or password is incorrect.\n Try again')
    conn.commit()
    conn.close()


