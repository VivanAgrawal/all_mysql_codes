import mysql.connector as connector
con=connector.connect(host='localhost', user='root',password='1234',database='mysqlconnect')
print(con)

