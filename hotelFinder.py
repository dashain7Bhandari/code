import sqlite3
conn=sqlite3.connect(database='HotelInfo.db')

my_cursor=conn.cursor()

class hotelFinder:
    def __init__(self,location,maxPrice,rating):
        self.location=location
        self.maxPrice=maxPrice
        self.rating=rating
    
    def search(self):
        select_cmd= '''SELECT * FROM Hotels WHERE location  = "{var1}" AND rating="{var2}" AND maxPrice<="{var3}" '''.format(var1=self.location,var2=self.rating,var3=self.maxPrice)
        self.result=my_cursor.execute(select_cmd)
        for data in self.result:
            
            print('The available hotels based on your search are \n')
            print(f"Name:{data[1]}")
            print(f"Location:{data[0]}")
            print(f"Stars rating:{data[2]}")
            print(f"Price of hotel room:{data[3]}")
            print('\n')

        conn.commit()
        

   #main  

from Login import logInDetails

if(logInDetails()==1):
    print('WELCOME TO NEPAL!!!!\n')

    def setLocation():
        while(True):
            location=input('Please enter the location you want to stay in.\n')

            if location.capitalize()!="Kathmandu" and location.capitalize()!="Bhaktapur" and location.capitalize()!="Lalitpur":
                print("Incorrect location.\n You can only search in Kathmandu,Lalitpur or Bhaktapur.")

            else:  
                return location.capitalize()

    def setRating():
        count=0
        while(True):
            rate=int(input('Please enter your rating preference of the hotel(Star).\n'))

            if rate!=2 and rate !=3 and rate != 4 and rate!=5:
                print("\nThere are only two star, three star, four star and five star hotels.Try again")
                    
            else:  
                return rate
        
    
        
    def setPrice():
        price=input('Enter maximum price you are willing to pay for a room per day\n')
        return int(price)


    # loc=setLocation()
    # rate=setRating()
    # Price=setPrice()
    # requiredHotel= hotelFinder(loc,rate,Price)
    # requiredHotel.search()

    choice="YES"
    while(choice.upper()=='YES'):

        loc=setLocation()
        rate=setRating()
        Price=setPrice()
        select_cmd= '''SELECT * FROM Hotels WHERE location  = "{var1}" AND rating="{var2}" AND maxPrice<="{var3}" '''.format(var1=loc,var2=rate,var3=Price)
        result=my_cursor.execute(select_cmd)
        count=0
        for data in result:
            count+=1     
            if count==1:
                print('\n')
                print('The available hotels based on your search are \n')

            print(f"Name:{data[1]}")
            print(f"Location:{data[0]}")
            print(f"Stars rating:{data[2]}")
            print(f"Price of hotel room:{data[3]}")
            print('\n')
        if(count==0):
            print('\n\nSorry,there are no such available hotels.\n Do you want to look for something else?')
            choice=input('Enter "YES" or "NO" ')
        else:
            break
        
    
conn.commit()
conn.close()

