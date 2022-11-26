import sqlite3
conn=sqlite3.connect(database='HotelInfo.db')

my_cursor=conn.cursor()

# create_table='''CREATE TABLE Hotels(location VARCHAR(15),name VARCHAR(25) NOT NULL,rating INT NOT NULL,maxPrice REAL CHECK (maxPrice>0))'''
# my_cursor.execute(create_table)


# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Marriott',5,30000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Hyatt Regency',5,25000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Tiger Palace',4,12000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Red Villa',4,15000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Blue Moon',3,5000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Himalayan',3,4000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Kathmandu','Sansri',2,2000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Lalitpur','ACube',4,16000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Lalitpur','Genesis',4,18000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Lalitpur','Queen',3,5000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Lalitpur','Aarnaya',3,6000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Lalitpur','Hessed',2,2500)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Bhaktapur','Juju',4,10000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Bhaktapur','Baaldari',4,14000)'''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Bhaktapur','Nirashi',3,4000) '''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Bhaktapur','Lumanti',3,6000) '''
# my_cursor.execute(insert_script)
# insert_script='''INSERT INTO Hotels VALUES ('Bhaktapur','Lahana',2,1500) '''
# my_cursor.execute(insert_script)
