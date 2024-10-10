import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost', port='3306',user='root',password='1234',database='mysqlconnect')
        query='create table if not exists user(userId int primary key, userName varchar(200),phone varchar(12) )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

     #insert
    def insert_user(self,userid,username,phone):
        query="insert into user(userId, userName, phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
        
    def update_user(self, userId, userName, phoneNumber):
        query = "update user set userName='{}', phone='{}' where userId={}".format(userName, phoneNumber, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")

#object of helper
helper=DBHelper()
helper.update_user(1423,"rahul","2222")
helper.insert_user(1442,"shashank","7755")
helper.insert_user(1264,"rohan","3214")
helper.insert_user(4569,"rajesh","8901")
