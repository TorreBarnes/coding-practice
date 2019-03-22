import MySQLdb
import pprint
import sys
from datetime import time, datetime
from _mysql import NULL


# Open database connection
database = MySQLdb.connect("160.111.103.59","barnestd","barnestd","names_joel" )

# prepare a cursor object using cursor() method
cursor = database.cursor() #(MySQLdb.cursors.DictCursor)

# execute SQL query using execute() method.
#cursor.execute("SELECT Name FROM names")

# Fetch names column from database using execute("query statement") method.
#data = cursor.fetchall()

# Each record must have a name. Each record may also have a birth year, death year, and/or id.   
    
# a function that accepts a dict "values" and a series of nested functions called on a case by case basis

values = {"name": None, "birth": None, "death": None, "viaf": None, 
          "remote_db": None, "remote_db_id": None}


def query_name(str): #Prints copy of results
    
    """
    Querying Database: Boolean
    
    -----------------------------------------------------------------------------
    This function...
     - accepts the argument values which is a dictionary that holds the keys: name, birth, death, and viaf provided by the user input recieved from the html form 
     - queries the database by selecting/matching the rows from the database table that correspond to the input the user provides.
     - will return all matching records just in case duplicates exist 
     
     LOGIC: 
     Did the user submit least one Authority ID?
        Yes, Search by Authority ID(s) (VIAF). Found a match?
            Yes, Return the Record
            No, Return no match on VIAF 
        No,  Search by Name, Birth, and or Death Found a Match?
            Yes. Return the Record
            No. Return no matches found

    """ 
   
    where = []
    vals = []
    
    
    if values["viaf"]:
        where.append("VIAF")
        vals.append(values["viaf"])
        
        sql = "SELECT Name FROM names WHERE " + where[0] + " = %s"
        # print (vals)
        # print (sql)
        cursor.execute(sql, vals)
        
        rec = cursor.fetchone()
        # pprint.pprint(rec)

        if rec == None:
            # print "System found no match on VIAF."
            return False
            
        else: 
            # print("Match found on viaf")
            return True   
    
    
    if values["name"]:
        where.append("Name")
        vals.append(values["name"])
        

    if values["birth"]:
        where.append("BirthYear")
        vals.append(values["birth"])
     

    if values["death"]:
        where.append("DeathYear")
        vals.append(values["death"])
    

    if len(where):
        sql = "SELECT Name, BirthYear, DeathYear, VIAF FROM names WHERE " + " = %s AND ".join(where) + " = %s"
        # print (vals)
        # print (sql)
        cursor.execute(sql, vals)
    else:
        # print"Error: No data recieved from user."
        sys.exit()

    rec = cursor.fetchall()
    # pprint.pprint(rec)

    if rec == None:
        # print "No results."
        return False
    else: 
        # print "Record(s) Found!"
        return True


def submit_name(str): #Prints copy of submitted record
    """
    Submitting Name: Boolean

    -----------------------------------------------------------------------------
        Based on data entered by user...
        
        - check if unique authority ID
            - Query database and compare user input to data stored
        - If not unique search by birth/death date for match
            - Query database and compare user input to data stored
        - If no match found create new record in database with input from user
    
    queryRecord()
        - boolean returns T/F based on if match found in database
    updateRecord()
        - void updates record by overwriting previous information entered 
    addRecord()
        - boolean returns T/F whether record/row was successfully added to database or not
        
    LOGIC:
    Did the user submit a name, a remote database name and a remote database id?
        No, return an error
    Did the user submit least one Authority ID?
        Yes, Search by Authority ID(s) (VIAF). Found a match?
            Yes, Update the Record
                Record the Log
                Return
            No, Add a record 
               Record the Log 
               Return
        No,  Search by Name+Birth+Death. Found a Match?
            Yes. Update the Record 
                Record the Log 
                Return
            No. Add a record 
               Record the Log 
               Return

    
    """
    

  
    def queryRecord(str):
        
            
        where = []
        vals = []
        
        
        if values["viaf"]:
            where.append("VIAF")
            vals.append(values["viaf"])
            
            sql = "SELECT Name FROM names WHERE " + where[0] + " = %s"
            # print (vals)
            # print (sql)
            cursor.execute(sql, vals)
            
            rec = cursor.fetchone()
            # pprint.pprint(rec)

            if rec == None:
                # print "System found no match on VIAF."
                return False
            else: 
                # print("Match found on viaf")
                return True   
        
        elif values["name"] and values["birth"] and values["death"]:
            where = []
            vals = []
            where.append("Name")
            where.append("BirthYear")
            where.append("DeathYear")
            vals.append(values["name"])
            vals.append(values["birth"])
            vals.append(values["death"])
            sql = "SELECT Name FROM names WHERE " + " = %s AND ".join(where) + " = %s"
            # print (vals)
            # print (sql)
            cursor.execute(sql, vals)
            
            rec = cursor.fetchone()
            # pprint.pprint(rec)

            if rec == None:
                # print "System found no match on name + life years."
                return False
            else: 
                # print "Match found on name + life years."
                return True
    
    
    def updateRecord():
        where = []
        vals1 = []
        vals2 = []
       

            
        if values["viaf"]:
            where.append("VIAF")
            vals2.append(values["viaf"])
            if values["birth"] and values ["death"]:
                #where.append("BirthYear")
                vals1.append("BirthYear")
                vals2.append(values["birth"])
                vals1.append("DeathYear")
                vals2.append(values["death"])
                sql = "UPDATE names SET " + " = %s, ".join(vals1) + " = %s" + " WHERE " + " = %s AND ".join(where) + " = %s"
                # print (vals1)
                # print (vals2)
                # print (sql)
                cursor.execute(sql, vals2)
                database.commit()
                # print "updated main record matched on viaf+birth+death"
                
                cursor.execute("SELECT id FROM names WHERE VIAF = %s", [values["viaf"]])
                Names_ID = cursor.fetchone()
                database.commit()
            
                if not Names_ID:
                    Names_ID[0] = 0
                
                cursor.execute("SELECT Name FROM names WHERE id = %s", [Names_ID[0]])
                Pref_Name = cursor.fetchone()
                
                if Pref_Name and values["name"] != Pref_Name[0]:
                    # print("Names do not match. Recording name submission as an alias")
                    cursor.execute("SELECT alias FROM aliases WHERE alias = %s AND names_id = %s;", [values["name"], Names_ID[0]])
                    isAlias = cursor.fetchone()
                    # pprint.pprint(isAlias)
                    
                    if isAlias:
                        # print("Alias already in table.")
                        return True
                    elif not isAlias:
                        # print("Alias not found in table. Adding alias...")
                        cursor.execute("INSERT INTO aliases (names_id, alias) VALUES (%s, %s);", [Names_ID[0], values["name"]])
                        database.commit()

                        cursor.execute("SELECT LAST_INSERT_ID()")
                        Alias_ID = cursor.fetchone()

                        cursor.execute("SELECT LAST_INSERT_ID()")
                        Alias_ID = cursor.fetchone()

                        action = "Added Name to Alias Table"
                        #notes = raw_input("Notes: ")
                        cursor.execute("INSERT INTO log (names_id, action, notes) VALUES (%s, %s, %s);", [Names_ID[0], action, Alias_ID[0]])
                        database.commit()
                
                # print("Adding record to remote_db table")
                try:
                    cursor.execute("INSERT INTO remote_dbs (names_id, source_name, source_id) VALUES (%s, %s, %s)", [Names_ID[0], values["remote_db"], values["remote_db_id"]])
                    database.commit()
                except:
                    print "We've seen this name before!", Names_ID[0]
                
                ###########################################
                #INSERT LOG UPDATE STATEMENTS HERE
                ###########################################
                action = "Updated Name"
                #notes = raw_input("Notes: ")
                cursor.execute("INSERT INTO log (names_id, action) VALUES (%s, %s);", [Names_ID[0], action])
                database.commit()
                
                return True
            
            elif values["birth"] and not values["death"]:
                #where.append("DeathYear")
                vals1.append("BirthYear")
                vals2.append(values["birth"])
                sql = "UPDATE names SET " + " = %s, ".join(vals1) + " = %s" + " WHERE " + " = %s".join(where) + " = %s"
                # print (vals1)
                # print (vals2)
                # print (sql)
                cursor.execute(sql,[vals2[1], vals2[0]])
                database.commit()
                # print "updated main record matched on viaf+birth"
                
                cursor.execute("SELECT id FROM names WHERE VIAF = %s", [values["viaf"]])
                Names_ID = cursor.fetchone()
                #print Names_ID[0]
                database.commit()
                
                if not Names_ID:
                    Names_ID[0] = 0
                    
                cursor.execute("SELECT Name FROM names WHERE id = %s", [Names_ID[0]])
                Pref_Name = cursor.fetchone()
                
                if Pref_Name and values["name"] != Pref_Name[0]:
                    # print("Names do not match. Recording name submission as an alias")
                    cursor.execute("SELECT alias FROM aliases WHERE alias = %s AND names_id = %s;", [values["name"], Names_ID[0]])
                    isAlias = cursor.fetchone()
                    # pprint.pprint(isAlias)
                    
                    if isAlias:
                        # print("Alias already in table.")
                        return True
                    elif not isAlias:
                        # print("Alias not found in table. Adding alias...")
                        cursor.execute("INSERT INTO aliases (names_id, alias) VALUES (%s, %s);", [Names_ID[0], values["name"]])
                        database.commit()
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        Alias_ID = cursor.fetchone()

                        action = "Added Name to Alias Table"
                        #notes = raw_input("Notes: ")
                        cursor.execute("INSERT INTO log (names_id, action, notes) VALUES (%s, %s, %s);", [Names_ID[0], action, Alias_ID[0]])
                        database.commit()
                
                # print("Adding record to remote_db table")
                cursor.execute("INSERT INTO remote_dbs (names_id, source_name, source_id) VALUES (%s, %s, %s)", [Names_ID[0], values["remote_db"], values["remote_db_id"]])
                database.commit()
                
                ###########################################
                #INSERT LOG UPDATE STATEMENTS HERE
                ###########################################
                action = "Updated Name"
                #notes = raw_input("Notes: ")
                cursor.execute("INSERT INTO log (names_id, action) VALUES (%s, %s);", [Names_ID[0], action])
                database.commit()
                
                return True
                
            
            elif values["death"] and not values["birth"]:
                #where.append("DeathYear")
                vals1.append("DeathYear")
                vals2.append(values["death"])
                sql = "UPDATE names SET " + " = %s, ".join(vals1) + " = %s" + " WHERE " + " = %s".join(where) + " = %s"
                # print (vals1)
                # print (vals2)
                # print (sql)
                cursor.execute(sql,[vals2[1], vals2[0]])
                database.commit()
                # print "updated main record matched on viaf+death"
                cursor.execute("SELECT id FROM names WHERE VIAF = %s", [values["viaf"]])
                Names_ID = cursor.fetchone()
                database.commit()
                
                if not Names_ID:
                    Names_ID[0] = 0
                    
                cursor.execute("SELECT Name FROM names WHERE id = %s", [Names_ID[0]])
                Pref_Name = cursor.fetchone()
                
                if Pref_Name and values["name"] != Pref_Name[0]:
                    # print("Names do not match. Recording name submission as an alias")
                    cursor.execute("SELECT alias FROM aliases WHERE alias = %s AND names_id = %s;", [values["name"], Names_ID[0]])
                    isAlias = cursor.fetchone()
                    # pprint.pprint(isAlias)
                    
                    if isAlias:
                        # print("Alias already in table.")
                        return True
                    elif not isAlias:
                        # print("Alias not found in table. Adding alias...")
                        cursor.execute("INSERT INTO aliases (names_id, alias) VALUES (%s, %s);", [Names_ID[0], values["name"]])
                        database.commit()
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        Alias_ID = cursor.fetchone()

                        action = "Added Name to Alias Table"
                        #notes = raw_input("Notes: ")
                        cursor.execute("INSERT INTO log (names_id, action, notes) VALUES (%s, %s, %s);", [Names_ID[0], action, Alias_ID[0]])
                        database.commit()
                
                # print("Adding record to remote_db table")
                cursor.execute("INSERT INTO remote_dbs (names_id, source_name, source_id) VALUES (%s, %s, %s)", [Names_ID[0], values["remote_db"], values["remote_db_id"]])
                database.commit()
                
                ###########################################
                #INSERT LOG UPDATE STATEMENTS HERE
                ###########################################
                action = "Updated Name"
                #notes = raw_input("Notes: ")
                cursor.execute("INSERT INTO log (names_id, action) VALUES (%s, %s);", [Names_ID[0], action])
                database.commit()
                return True
            
            
                
            
            
            
        if values["name"] and values["birth"]and values["death"]:
            #where.append("BirthYear")
            vals1.append("BirthYear")
            vals2.append(values["birth"])
            

            #where.append("DeathYear")
            vals1.append("DeathYear")
            vals2.append(values["death"])
            
            where.append("Name")
            vals2.append(values["name"])

        
            
            if len(where):
                sql = "UPDATE names SET " + " = %s, ".join(vals1) + " = %s" + " WHERE " + " = %s AND ".join(where) + " = %s"
                # print (vals1)
                # print (vals2)
                # print (sql)
                cursor.execute(sql, vals2)
                database.commit()
                
            cursor.execute("SELECT id FROM names WHERE Name = %s AND BirthYear = %s AND DeathYear = %s", [values["name"], values["birth"], values["death"]])
            Names_ID = cursor.fetchone()
            #Names_ID = cursor.lastrowid()
                
                
            database.commit()
        
            if not Names_ID:
                Names_ID[0] = 0
        
            # print("Adding record to remote_db table")
            cursor.execute("INSERT INTO remote_dbs (names_id, source_name, source_id) VALUES (%s, %s, %s)", [Names_ID[0], values["remote_db"], values["remote_db_id"]])
            database.commit()
            
            ###########################################
            #INSERT LOG UPDATE STATEMENTS HERE
            ###########################################
            action = "Updated Name"
            #notes = raw_input("Notes: ")
            cursor.execute("INSERT INTO log (names_id, action) VALUES (%s, %s);", [Names_ID[0], action])
            database.commit()
        
         
            
    def addRecord():
        where = []
        vals = []
        count = 0
        
        
        if values["name"]:
            where.append("Name")
            vals.append(values["name"])
            count+=1

        if values["birth"]:
            where.append("BirthYear")
            vals.append(values["birth"])
            count+=1

        if values["death"]:
            where.append("DeathYear")
            vals.append(values["death"])
            count+=1

        if values["viaf"]:
            where.append("VIAF")
            vals.append(values["viaf"])
            count+=1
      
        if len(where):
            #print("COUNT IS ", count)
            #if count == 1:
            #    sql = "INSERT INTO names (" + ", ".join(where) + ") VALUES (" + "%s"+ (count)*(" %".join(",s")) +") " 
            #    # print(sql)
            #else:
            sql = "INSERT INTO names (" + ", ".join(where) + ") VALUES (" + "%s"+ (count-1)*(" %".join(",s")) +") " 
            # print (vals)
            # print (sql)
            cursor.execute(sql, vals)
            
            #cursor.execute("INSERT INTO remote_dbs (names_id) VALUES (LAST_INSERT_ID())")
            #Names_ID = cursor.LAST_INSERT_ID()
            database.commit()
        
        #if not Names_ID:
            #Names_ID[0] = 1
        
        # print("Adding record to remote_db table")
        cursor.execute("SELECT LAST_INSERT_ID()")
        Names_ID = cursor.fetchone()

        sql = "INSERT INTO remote_dbs (names_id, source_name, source_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, [Names_ID[0], values["remote_db"], values["remote_db_id"]])
        database.commit()
        
        ###########################################
        #INSERT LOG UPDATE STATEMENTS HERE
        ###########################################
        action = "Added Name"
        #notes = raw_input("Notes: ")
        sql = "INSERT INTO log (names_id, action) VALUES (%s, %s)"
        cursor.execute(sql, [Names_ID[0], action])
        database.commit()
        
        #print(result)
        return True
    
    error = "Submission did not include name, remote database name, and remote database ID."
    if not values["name"] or not values["remote_db"] or not values["remote_db_id"]:
            # print error
            return False
            
    cursor.execute("SELECT VIAF FROM names WHERE VIAF = %s", [values["viaf"]])
    ID = cursor.fetchone()
    
    RecordFound = queryRecord(values)
    
    if RecordFound and values["viaf"]:
        if values["viaf"] and int(values["viaf"]) == ID[0]:
            #print "Updating record (Location: logic 1)"
            return updateRecord()
    
    
    elif RecordFound and not values["viaf"]:
        #print("Updating record (Location: logic 2)")
        return updateRecord()
    
    elif not RecordFound and not values["remote_db"] and not values["remote_db_id"]:
        # print(error)
        return False
    
    elif not RecordFound and not values["remote_db"] and values["remote_db_id"]:
        # print(error)
        return False 
    
    elif not RecordFound and values["remote_db"] and not values["remote_db_id"]:
        # print (error)
        return False
    
    elif not RecordFound and values["remote_db"] and values["remote_db_id"] and not values["viaf"]:
        #print("adding record logic 1")
        return addRecord()
        
    elif not RecordFound and values["remote_db"] and values["remote_db_id"] and values["viaf"]:
        #print("adding record logic 2")
        return addRecord()
        
    
    else:
        # print("did nothing")
        return False
    


