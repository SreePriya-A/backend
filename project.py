import MySQLdb
getnode(123467809)
def getnode(Id):
    db = MySQLdb.connect("localhost","Sri","Sri@1204","sample" )
    cursor = db.cursor()
    cursor.execute("SELECT parent from dummy where id=Id")
    data = cursor.fetchone()
    if data>100000000:
      getnode(data)
    else:
        getlocation(data)
def getlocation(node):
    db = MySQLdb.connect("localhost","Sri","Sri@1204","sample" )
    cursor = db.cursor()
    cursor.execute("SELECT location from locMap where node=Node")
    data = cursor.fetchone()
    return data
def updatenode(Id):
      
    