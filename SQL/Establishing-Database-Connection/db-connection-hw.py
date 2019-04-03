import sqlite3
import pprint
import sys



# Open database connection
database = sqlite3.connect("JobSearch.db")

# prepare a cursor object using cursor() method
cursor = database.cursor() #(MySQLdb.cursors.DictCursor)

# execute SQL query using execute() method.
#cursor.execute("SELECT Name FROM names")

# Fetch names column from database using execute("query statement") method.
#data = cursor.fetchall()   
    

def queryRecord():
    
    
    print("1. Find the names of all companies hiring in Atlanta\n")
    print("2. How many applicants have a resume online.\n")
    print("3. Display all jobs in the zipcode 30238.\n")
    print("4. Display all companies hiring for a position.\n")
    print("5. Display all applicants available in Alabama.\n")

    
    print("Make a selction (1 - 5) or 0 to exit: ")
    choice = raw_input()
    if (choice == '1'):
        sql = "SELECT name FROM Companies WHERE (City = 'Atlanta');"
        cursor.execute(sql)
        rec = cursor.fetchall()
        pprint.pprint(rec)
        
    if (choice == '2'):
        sql = "SELECT COUNT(resume/cv) FROM Applicants WHERE resume/cv LIKE '%yes%';"
        cursor.execute(sql)
        rec = cursor.fetchone()
        pprint.pprint(rec)

    if (choice == '3'):
        sql = "SELECT description, name FROM Companies WHERE zip = 30238;"
        cursor.execute(sql)
        rec = cursor.fetchall()
        pprint.pprint(rec)

    if (choice == '4'):
        sql = "SELECT name FROM Companies;"
        cursor.execute(sql)
        rec = cursor.fetchall()
        pprint.pprint(rec)

    if (choice == '5'):
        sql = "SELECT fname, lname FROM Applicants WHERE city = Alabama"
        cursor.execute(sql)
        rec = cursor.fetchall()
        pprint.pprint(rec)

run = True                  
while (run):
    queryRecord()
    print("Run again? y/n")
    run = raw_input()
    if run == 'y':
        run = True
    else:
        break
    


                  
            
  
    
    
   
