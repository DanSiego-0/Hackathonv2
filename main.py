import pymysql
import barcode
import func as fn

pymysql.install_as_MySQLdb()





# Database (Change nalang ung user and pass)
admin_host = "localhost"
admin_Username = "root" 
admin_Password = "brendanc"
admin_db = "healthi"

connection = pymysql.connect(host=admin_host,user=admin_Username,password=admin_Password,database=admin_db)
cursor = connection.cursor()



answer = input("What product would you like to learn about?: ")

query = f"SELECT Product FROM products WHERE Product = '{answer}'"

imageloc = 'barcode.gif'
barcode.decode(imageloc)



cursor.execute(query)
data = cursor.fetchone()
data = fn.Clean(data)
print(data)
print(fn.ReturnFact(data))
connection.close()





