from curses import window
import pymysql
import barcode
import func as fn
from tkinter import * 

pymysql.install_as_MySQLdb()






# Database (Change nalang ung user and pass)
admin_host = "localhost"
admin_Username = "root" 
admin_Password = "brendanc"
admin_db = "healthi"


# Establish connection
connection = pymysql.connect(host=admin_host,user=admin_Username,password=admin_Password,database=admin_db)
cursor = connection.cursor()


def SearchQuery(query):
    try:
        query = f"SELECT Product FROM products WHERE Product = '{query}'"
        cursor.execute(query)
        data = cursor.fetchone()
        data = fn.Clean(data)
        return data
    except:
        return None
    

def NutriFacts(product):
    return fn.ReturnFact(product)

def BarcodeReader(image):
    return barcode.BarcodeReader(image)



connection.close()





