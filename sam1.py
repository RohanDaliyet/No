import pymysql

connection=None

def getSqlConnection():
    global connection
    if connection is None:
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="emotions_tracker")
        #connection = pymysql.connect(host="ec2-13-126-160-81.ap-south-1.compute.amazonaws.com", user="root",passwd="Bl00dM00n@2017", database="emotifics")
    return connection

