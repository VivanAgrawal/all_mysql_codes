import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost', port='3306',user='root',password='1234',database='mysqlconnect')
        query='create table if not exists user(userId int primary key, userName varchar(200),phone varchar(12) )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    
    def delete_user(self,userId):
        query="delete from user where userId= {}".format(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

#object of helper
helper=DBHelper()
helper.delete_user(1234)
