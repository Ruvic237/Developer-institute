# Perform operations on database using python
from ast import If
import psycopg2
HOSTNAME = "localhost"
DATABASE = "Restaurant"
USERNAME = "postgres"
PASSWORD = "Copyright1"

class MenuItem :
    
    #method to be called to modify database
    def run_query(self,query):
        
        # making the connection to the database
        connection = psycopg2.connect(host = HOSTNAME,dbname = DATABASE,user = USERNAME,password = PASSWORD ) 
        
        # collecting database info to do query
        cursor = connection.cursor()
        
        #Execution of the query as parameter
        cursor.execute(query)
        
        #Commit to consider any change of database and close database
        connection.commit()
        connection.close()
        
    #instantiating using the dunder method
    def __init__(self,names,prices):
        self.name = names
        self.price = prices
    
    #a method to save or add rows in a table
    def save(self):
        query = f"INSERT INTO resto(name,price) VALUES('{self.name}',{self.price})"
        
        #to call method use self prefix
        self.run_query(query)
    
    #a method to delete row from table    
    def delete(self):
        query = f"DELETE FROM resto where name = '{self.name}' "
        self.run_query(query)
        
    #A method to update existing items in database
    def update(self,new,prix):
        query = f"UPDATE resto SET name = '{new}',price = {prix} Where name = '{self.name}'and price = {self.price}"
        self.run_query(query)
        
    def all():     
        # making the connection to the database 
        connection1 = psycopg2.connect(host = HOSTNAME,dbname = DATABASE,user = USERNAME,password = PASSWORD)
        
        # collecting database info to do query 
        cursor1 = connection1.cursor()
        
        #making a request from database
        queryall = "SELECT * FROM resto"
        
        #executing the request command in database
        cursor1.execute(queryall)
        
        #fetching all items and storing in result 
        results = cursor1.fetchall()
        
        #closing the connection
        connection1.close()
        
        #itirating through every item stored in result
        for move in results:
            print(move)
            
    def get_item(self,new):
       if new == self.name: 
        # making the connection to the database 
        connection1 = psycopg2.connect(host = HOSTNAME,dbname = DATABASE,user = USERNAME,password = PASSWORD)
        
        # collecting database info to do query 
        cursor1 = connection1.cursor()
        
        #making a request from database
        query = f"SELECT name,price FROM resto Where name = '{new}'"
            
        #executing the request command in database
        cursor1.execute(query)
        
        #fetching all items and storing in result 
        results = cursor1.fetchall()
        
        #closing the connection
        connection1.close()
        
        
        #itirating through every item stored in result
        for move in results:
            print(move)
       else:
            print("no item matches try again")
        
      
        
item = MenuItem('Burger',35)
item1 = MenuItem('shawama',25)
item2 = MenuItem('Bread',15)
# item.save()
# item1.save()
# item2.save()
# item.update('Veggie Burger',37)
# item5 = MenuItem.all()
# item2.get_item('Brea')




    
    