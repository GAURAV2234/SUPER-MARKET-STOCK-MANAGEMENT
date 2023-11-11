# STOCK MANAGEMENT

import os, sys, datetime, time

##Downloading Missing Modules
try:
    import mysql.connector
except:
    os.system('cls')
    print('\n\tDOWNLOADING MISSING MODULE : mysql.connector :\n')
    os.system('cmd /c "pip install mysql-connector"')
    import mysql.connector
    os.system('cls')
try:
    from stdiomask import getpass
except:
    os.system('cls')
    print("\n\tDOWNLOADING MISSING MODULE : stdiomask :\n")
    os.system('cmd /c "pip install stdiomask"')
    from stdiomask import getpass
    os.system('cls')
try:
    import art
except:
    os.system('cls')
    print('\n\tDOWNLOADING MISSING MODULE : art :\n')
    os.system('cmd /c "pip install art"')
    from art import text2art
    os.system('cls')



##DATABASE MANAGEMENT
def db_mgmt():
    while True:
        p = query("database - management", ['Database creation',
                                            'List Database',
                                            'Format/Reset Database',
                                            'home'])
        if p == 1:
            create_db()
        if p == 2:
            list_db()
        if p == 3:
            del_db()
        if p == 4:
            clean()
            run()

def create_db():
    clean()
    try:
        mycursor.execute("select * from orders;")
        print('\n\n\n\t\t\tTables Already Exist...')
        clean(1)
    except:
        load_efct("Creating PRODUCT table")
        sql = "CREATE TABLE if not exists product (\
                      pcode int(4) PRIMARY KEY,\
                      pname char(40) NOT NULL,\
                      pprice float(10,2) ,\
                      pqty int(10) ,\
                      pcat char(40));"
        mycursor.execute(sql)

        load_efct("Creating ORDER table")
        sql = "CREATE TABLE if not exists orders (\
                      orderid int(4)PRIMARY KEY ,\
                      orderdate DATE ,\
                      pcode char(30) NOT NULL , \
                      pprice float(10,2) ,\
                      pqty int(4) ,\
                      supplier char(50),\
                      pcat char(40));"
        mycursor.execute(sql)

        load_efct("Creating SALES table")
        sql = "CREATE TABLE if not exists sales (\
                      salesid int(4) PRIMARY KEY ,\
                      salesdate DATE ,\
                      pcode char(30) references product(pcode), \
                      pprice float(8,2) ,\
                      pqty int(7) ,\
                      Total double(8,2)\
                      );"
        mycursor.execute(sql)

        load_efct("Creating USER table")
        sql = "CREATE TABLE if not exists user (\
                      uid int(4) PRIMARY KEY,\
                      uname char(50) NOT NULL,\
                      upwd char(50));"
        mycursor.execute(sql)
        print("\n\n\n\t\t\tAll table created SUCCESSFULLY")
        clean(1.5)

def list_db():
    clean()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("show tables;")
    n=1
    for i in mycursor:
        print("\n","\t"*5,n,i[0].upper())
        n+=1
    print("\n","\t" * 4, "TOTAL TABLES :",n-1)
    input('\n\tPress ENTER to return - ')
    clean()

def del_db():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    xn = input('\n\tAre you sure you want to format the database (Y/N) : ')
    if xn.lower() == 'y':
        mycursor.execute('drop table orders,product,sales,user;')
        load_efct('Resetting all tables')
        clean()
    elif xn.lower() == 'n':
        clean(.5)
    else:
        print("\tWrong Choice")


##USER MANAGEMENT

def user_mgmt():
    clean()
    while True:
        u = query("user - management",
                  ["add user",
                   "list user",
                   'remove user',
                   "home"])
        if u == 1:
            add_user()
        if u == 2:
            list_user()
        if u == 3:
            del_usr()
        if u == 4:
            clean()
            break

def add_user():
    uid =   input("\nEnter ID (Four Digits) : ")
    name =  input("Enter Name             : ")
    paswd = input("Enter Password         : ")
    sql = "INSERT INTO user values (%s,%s,%s);"
    val = (uid, name, paswd)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\nUser added")
    clean(.5)

def list_user():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT uid,uname from user")
    clean()
    print("\t\t\t\tUSER DETAILS")
    print("\t\t", "-" * 27)
    print("\t\t UID        name    ")
    print("\t\t", "-" * 27)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1])
    print("\t\t", "-" * 27)
    input('\n\tPress ENTER to return - ')
    clean()

def del_usr():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    ID = int(input("\nEnter the User ID :"))
    mycursor.execute("select * from user;")
    for i in mycursor:
        if i[0] == ID:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("DELETE FROM user WHERE uid ="+str(ID)+';')
            mydb.commit()
            print("\nUser removed successfully.")
            break
    else:
        print("\nUser with ID", ID, "not found !")
    clean(.5)
    
##PRODUCT MANAGEMENT

def product_mgmt():
    clean()
    while True:
        p = query("product management",
                  ["add new product",
                   "list products",
                   "search products",
                   "update products",
                   "delete products",
                   "home"])
        if p == 1:
            add_prod()
        if p == 2:
            list_prod()
        if p == 3:
            search_prod()
        if p == 4:
            update_pqty()
        if p == 5:
            del_prod()
        if p == 6:
            clean()
            break

def add_prod():
    sql = "INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
    code = int(input("\n\t\tEnter product code :"))
    search = "SELECT count(*) FROM product WHERE pcode=%s;"
    val = (code,)
    mycursor.execute(search, val)
    for x in mycursor:
        cnt = x[0]
    if cnt == 0:
        name = input('\t\tEnter product name :')
        qty = int(input("\t\tEnter product quantity :"))
        price = float(input("\t\tEnter product unit price :"))
        cat = input("\t\tEnter product category :")
        val = (code, name, price, qty, cat)
        mycursor.execute(sql, val)
        mydb.commit()
        print('\n1 product added')
    else:
        print("\n\t\tProduct with code",code,"already exists !")
    clean(.5)

def update_pqty():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    code = int(input("\nEnter the product code :"))
    mycursor.execute("select * from product")
    for i in mycursor:
        if i[0] == code:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
            mycursor = mydb.cursor(buffered=True)
            print("\nOld Quantity : ",i[3])
            qty = int(input("Enter the NEW quantity :"))
            sql = "UPDATE product SET pqty=%s WHERE pcode=%s;"
            val = (qty, code)
            mycursor.execute(sql, val)
            mydb.commit()
            print("\n\t\t Product details updated")
            break
    else:
        print("\nProduct with code",code,"not found !")
    clean(.5)

def del_prod():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    code = int(input("\nEnter the product code :"))
    mycursor.execute("select * from product")
    for i in mycursor:
        if i[0] == code:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("DELETE FROM product WHERE pcode ="+str(code)+';')
            mydb.commit()
            print("\nRecord deleted successfully.")
            break
    else:
        print("\nProduct with code", code, "not found !")
    clean(.5)

def search_prod():
    clean()
    while True:
        s = query("search product",
                  ["list all products",
                   "search products code wise",
                   "search product category wise",
                   "back"])
        if s == 1:
            list_prod()
        if s == 2:
            srch_prcode(int(input("\n\tEnter product code :")))
        if s == 3:
            srch_prcat(input("\n\tEnter category :"))
        if s == 4:
            clean()
            break

def srch_prcode(code):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * from product WHERE pcode=%s"
    val = (code,)
    mycursor.execute(sql, val)

    print("\n\t\t\tPRODUCT DETAILS")
    print('\t',"-" * 48)
    print('\t '+'Code','Name','Price','Quantity','Category',sep='\t')
    print('\t',"-" * 48)
    for i in mycursor:
        print('\t '+str(i[0]),i[1],i[2],i[3],'\t'+i[4],sep='\t')
    print('\t',"-" * 48)
    input('\n\tPress ENTER to return - ')
    clean()

def srch_prcat(cat):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * from product WHERE pcat =%s"
    val = (cat,)
    mycursor.execute(sql, val)

    print("\n\t\t\tPRODUCT DETAILS")
    print('\t',"-" * 48)
    print('\t '+'Code','Name','Price','Quantity','Category',sep='\t')
    print('\t',"-" * 48)
    for i in mycursor:
        print('\t '+str(i[0]),i[1],i[2],i[3],'\t'+i[4],sep='\t')
    print('\t',"-" * 48)
    input('\n\tPress ENTER to return - ')
    clean()

def list_prod():
    clean()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * from product"
    mycursor.execute(sql)

    print("\n\n\t\t\tPRODUCT DETAILS")
    print('\t',"-" * 48)
    print('\t '+'Code','Name','Price','Quantity','Category',sep='\t')
    print('\t',"-" * 48)
    for i in mycursor:
        print('\t '+str(i[0]),i[1],i[2],i[3],'\t'+i[4],sep='\t')
    print('\t',"-" * 48)
    input('\n\tPress ENTER to return - ')
    clean()



##PURCHASE MANAGEMENT

def purchase_mgmt():
    clean()
    while True:
        o = query("purchase management",
                  ["add order",
                   "list orders",
                   'check demand',
                   "home"])
        if o == 1:
            add_order()
        if o == 2:
            list_order()
        if o == 3:
            chk_demand()
        if o == 4:
            clean()
            break

def add_order():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    now = datetime.datetime.now()
    sql = "INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values (%s,%s,%s,%s,%s,%s,%s)"
    code = int(input("\nEnter product code :"))
    oid = now.year + now.month + now.day + now.hour + now.minute + now.second
    qty = int(input("Enter product quantity : "))
    price = float(input("Enter Product unit price: "))
    cat = input("Enter product category: ")
    supplier = input("Enter Supplier details: ")
    val = (oid, now, code, price, qty, supplier, cat)
    mycursor.execute(sql, val)
    mydb.commit()
    print('\nOrder added SUCCESSFULLY.')
    clean(.5)

def list_order():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * from orders"
    mycursor.execute(sql)
    clean()
    print("\n\n\t\t\t\t\tORDER DETAILS")
    print('\t\t',"-" * 85)
    print("\t\t orderid    Date    Product code    price     quantity      Supplier      Category")
    print('\t\t',"-" * 85)
    for i in mycursor:
        print('\t\t '+str(i[0]), "\t", i[1], "\t", i[2], "\t   ", i[3], "\t", i[4], "\t     ", i[5], "\t", i[6])
    print('\t\t',"-" * 85)
    input('\n\tPress ENTER to return - ')
    clean()

def chk_demand():
    clean()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT pname,pcode from product where pqty = 0")
    print('\n\n\t\tFollowing Product(s) are DEMANDED:')
    for i in mycursor:
        print('\n\t\t',i[0],'(',i[1],')')
    input('\n\nPress ENTER to return - ')
    clean()

##SALES MANAGEMENT

def sales_mgmt():
    while True:
        s = query("sales -  management",["sale items",
                                         "list sales",
                                         "home"])
        if s == 1:
            sale_product()
        if s == 2:
            list_sale()
        if s == 3:
            clean()
            break

def sale_product():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    code = int(input("\nEnter product code: "))
    mycursor.execute('Select * from product')
    for i in mycursor:
        if i[0] == code:
            price = i[2]
            product = i[1]
            pqty = i[3]
            print(pqty,product,'availabe currently.\n')
            qty = int(input('Enter quantity to be sold : '))
            if qty <= pqty:
                print("\nCollect Rs.", qty * price)
                mycursor.execute('select salesid from sales;')
                global a
                a = 0
                for x in mycursor:
                    if x[0] > a:
                        a = x[0]
                sql = 'insert into sales values(%s,%s,%s,%s,%s,%s)'
                val = (a+1,datetime.date.today(),code,price,qty,price*qty)
                mycursor.execute(sql,val)
                mydb.commit()
                mycursor.execute('Update product set pqty = pqty -'+str(qty)+' where pcode ='+str(code)+';')
                mydb.commit()
                
            else:
                print("\nNot enough",product,'available !')
            input('\n\tPress ENTER to return - ')
            clean()
            break
    else:
        print('Product not found !')
        clean(.5)

def list_sale():
    clean()
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=key, database="stock")
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM sales"
    mycursor.execute(sql)
    print(" \t\t\t\tSALES DETAILS")
    print("-" * 80)
    print("Sales id    Date     Product Code     Price             Quantity           Total")
    print("-" * 80)
    for x in mycursor:
        print(x[0], "\t", x[1], "\t", x[2], "\t   ", x[3], "\t\t", x[4], "\t\t", x[5])
    print("-" * 80)
    input('\n\tPress ENTER to return - ')
    clean()



##Interface Elements

def query(title, tasks=[], tabs=3):
    x = len(title) + 4
    print("\t" * tabs, "-" * x)
    print("\t" * tabs, "|", title.upper(), "|")
    print("\t" * tabs, "-" * x,'\n')
    for i in tasks:
        print("\t" * (tabs - 1), tasks.index(i) + 1, i.upper(), "\n\n")
    return int(input("\tENTER\n\tYOUR\n\tCHOICE >  "))

def clean(waiting_time=0.0):
    time.sleep(waiting_time)
    os.system('cls')

def load_efct(text="Loading"):
    clean()
    print('\n'*4,'\t'*2, text, '.')
    clean(0.3)
    print('\n'*4,'\t'*2, text, '. .')
    clean(0.3)
    print('\n'*4,'\t'*2, text, '. . .')
    clean(0.4)

def intro():
    a = art.text2art('''    Stock
     - Fit -''', 'univers').split('\n')

    for i in a:
        print(i, end='\n')
        time.sleep(.1)
    # print('\t\t\t\t\tby Om Gupta')

##MAINPROGRAM
def run():
    try:
        while True:
            # clean()
            mydb = mysql.connector.connect(host="localhost", user="root", passwd=key)
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("create database if not exists stock;")
            mycursor.execute('use stock;')
            n = query(" stock management ", ["database setup",
                                             "user management",
                                             "product management",
                                             "purchase management",
                                             "sales management",
                                             "exit"])
            clean()
            if n == 1:
                db_mgmt()
            if n == 2:
                user_mgmt()
            if n == 3:
                product_mgmt()
            if n == 4:
                purchase_mgmt()
            if n == 5:
                sales_mgmt()
            if n == 6:
                a = art.text2art('''

 Thank You''','univers').split('\n')
                for i in a :
                    print(i,end='\n')
                    time.sleep(.1)
                clean(1)
                sys.exit()
    except Exception as e:
        print("\n\n", str(sys.exc_info()[0])[8::].replace("'>", "!"), e, ".\n\n")
        clean(3)

intro()
clean(1.7)
while True:
    clean()
    key = getpass(prompt="\nEnter mysql Password : ",mask="*")

    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd=key)
    except:
        print('\n\tInvalid Password! Try again.')
        time.sleep(.4)
        continue
    if mydb.is_connected():
        load_efct("Starting")
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd=key)
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute('create database if not exists stock;')
        mycursor.execute('use stock;')
        run()
