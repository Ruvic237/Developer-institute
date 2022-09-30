import psycopg2
import psycopg2.extras

HOSTNAME = "localhost"
DATABASE = "dvdrental"
USERNAME = "postgres"
PASSWORD = "Copyright1"

#To confirm my connection to the data base I use psycopg2.connect reserved word
connection = psycopg2.connect(host = HOSTNAME,dbname = DATABASE, user = USERNAME, password = PASSWORD)
 
#nOW TIME TO RETRIEVE information from the database to do a query with the aid of cursor
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

#Time to do a query request from data base
Query = "SELECT * FROM film LIMIT 10"

#Now (3) we need to execute the query using execute reserved word with the query inside the ()
cursor.execute(Query) #if we fetch one element use fetch1 below

#Now we need to fetch all in (3) using fetch method
results = cursor.fetchall()

#After all operation done e need to close the connection ()
connection.close()

#To display results we can use a for loop
for show in results:
    print(show)
 




