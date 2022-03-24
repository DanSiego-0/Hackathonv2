import pymysql

pymysql.install_as_MySQLdb()


def ConnectServer():
    # Database (Change nalang ung user and pass)
    admin_host = "localhost"
    admin_Username = "root" 
    admin_Password = "brendanc"
    admin_db = "healthi"

    connection = pymysql.connect(host=admin_host,user=admin_Username,password=admin_Password,database=admin_db,cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    query = "SELECT Product FROM products WHERE Product = 'Nido'"
    cursor.execute(query=query)
    data = cursor.fetchone()
    print(data)
    connection.close()

ConnectServer()



