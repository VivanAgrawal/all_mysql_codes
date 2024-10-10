import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost', port='3306',user='root',password='1234',database='pythontest')
        query='create table if not exists user(userId int primary key, userName varchar(200),phone varchar(12) )'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")

    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id:",row[0])
            print("User Name:",row[1])
            print("User Phone:",row[2])

#object of helper
helper=DBHelper()
helper.fetch_all()