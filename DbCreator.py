import sqlite3 as lite

con = None

con = lite.connect('Places.db')
con.text_factory = str
cur = con.cursor()    
cur.execute('SELECT SQLITE_VERSION()')
    
data = cur.fetchone()
    
print "SQLite version: %s" % data    

cur.execute('''CREATE TABLE IF NOT EXISTS
            Country (
            Id_Country INTEGER PRIMARY KEY,
            Country TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS
            State (
            Id_State INTEGER PRIMARY KEY,
            Id_Country INT,
            State TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS
            Region (
            Id_Region INTEGER PRIMARY KEY,
            Id_State INT,
            Region TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS
            City (
            Id_City INTEGER PRIMARY KEY,
            Id_Region INT,
            City TEXT)''')
def insert_country(country):
    cur.execute("select * from Country where Country = '%s'"%(country))
    foo = cur.fetchone()
    if foo == None:
        cur.execute("insert into Country(Country) VALUES('%s')"%(country))
        con.commit()
        cur.execute("select * from Country where Country = '%s'"%(country))
        foo = cur.fetchone()
        return foo
    else:
        return foo 

def insert_state(idCountry,state):
    cur.execute("select * from State where State = '%s' and Id_Country = %s"%(state, idCountry))
    foo = cur.fetchone()
    if foo == None:
        cur.execute("insert into State(Id_Country,State) VALUES(%s, '%s')"%(idCountry,state))
        con.commit()
        cur.execute("select * from State where State = '%s' and Id_Country = %s"%(state, idCountry))
        foo = cur.fetchone()
        return foo
    else:
        return foo   

def insert_region(idState,region):
    cur.execute("select * from Region where Region = '%s' and Id_State = %s"%(region, idState))
    foo = cur.fetchone()
    if foo == None:
        cur.execute("insert into Region(Id_State,Region) VALUES(%s, '%s')"%(idState,region))
        con.commit()
        cur.execute("select * from Region where Region = '%s' and Id_State = %s"%(region, idState))
        foo = cur.fetchone()
        return foo
    else:
        return foo

def insert_city(idRegion,city):
    cur.execute("select * from City where City = '%s' and Id_Region = %s"%(city,idRegion))
    foo = cur.fetchone()
    if foo == None:
        cur.execute("insert into City(Id_Region,City) VALUES(%s, '%s')"%(idRegion,city))
        con.commit()
        cur.execute("select * from City where City = '%s' and Id_Region = %s"%(city,idRegion))
        foo = cur.fetchone()
        return foo
    else:
        return foo

def insert_full(country, state, region, city):
    print insert_city(insert_region(insert_state(insert_country(country)[0],state)[0],region)[0],city)
    
    
f = open("raw.csv","r")
raw = f.read()
f.close()
linear = raw.split("\n")
for line in linear:
    fields= line.split(';')
    insert_full(fields[0],fields[1],fields[2],fields[3])


