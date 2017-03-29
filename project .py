import MySQLdb
getnode(123467809) #just to call a method
def getnode(Id):
    db = MySQLdb.connect("localhost","Sri","Sri@1204","sample" )
    cursor = db.cursor()
    cursor.execute("SELECT parent from dummy where id=Id")
    data = cursor.fetchone()
    if data>100000000:
      getnode(data)
    else:
        getlocation(data)
    db.close()
def getlocation(Node):
    db = MySQLdb.connect("localhost","Sri","Sri@1204","sample" )
    cursor = db.cursor()
    cursor.execute("SELECT location from locMap where node=Node")
    data = cursor.fetchone()
    db.close()
    return data
def updatenode(Id, Node):
    db = MySQLdb.connect("localhost","Sri","Sri@1204","sample" )
    cursor = db.cursor()
    cursor.execute("UPDATE dummy SET parent =Node WHERE id =Id")
    db.close()
    