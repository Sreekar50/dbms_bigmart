from p_5 import *
from p_4 import *

import mysql.connector

cid = 0
# connect to the database
BG = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sreekar@33",
  database="bigmart1"
)
cursor = BG.cursor()

def create_customer():
    print("Please enter your details:")
    fname = input("first Name: ")
    mname = input("middle Name: ")
    lname = input("last Name: ")
    address = input("Address: ")
    phone = int(input("mobile number: "))
    a_bal = int(input("account balance: "))
    s_type = input("subscription type: ")
    password = input("Password: ")
    
    
    cursor.execute("INSERT INTO customer (cus_firstname, cus_middlename,cus_lastname,cus_address,mobile_no, Account_Balance, Subcription_Type, cust_pswd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )", (fname, mname, lname, address, phone, a_bal, s_type, password))
    BG.commit()
    
    print("Customer created successfully! \n")

def cust_login():
    print("Please enter your login details:")
    phone = int(input("mobile number: "))
    password = input("Password: ")
    
    cursor.execute("SELECT * FROM customer WHERE mobile_no = %s AND cust_pswd = %s", (phone, password))
    result = cursor.fetchone()
    cid=result[0]
    if result:
        print(" customer Login successful!")
        return cid
    else:
        print("Invalid email or password.")
        return 0

def emp_login():
    print("Please enter your login details:")
    usr = input("username: ")
    password = input("Password: ")
    
    cursor.execute("SELECT * FROM employee WHERE emp_usr = %s AND emp_pswd = %s", (usr, password))
    result = cursor.fetchone()
   
    if result:
        print("employee Login successful!")
        return result[0]
    else:
        print("Invalid email or password.")
        return 0
    
def supp_login():
    print("Please enter your login details:")
    usr = input("username: ")
    password = input("Password: ")
    
    cursor.execute("SELECT SuppId FROM supplier WHERE sp_usr = %s AND sp_pswd = %s", (usr, password))
    result = cursor.fetchone()
   
    if result:
        print(" suplier Login successful!")
        return result[0]
    else:
        print("Invalid email or password.")
        return 0
    
def admin_login():
    print("Please enter your login details:")
    usr = input("username: ")
    password = input("Password: ")
    
    cursor.execute("SELECT AdminId FROM admin WHERE ad_usr = %s AND ad_pswd = %s", (usr, password))
    result = cursor.fetchone()
   
    if result:
        print("admin Login successful!")
        return result[0]
    else:
        print("Invalid email or password.")
        return 0

def add_to_cart():
    
    customer_id=cid
    
    # ask for the product ID and quantity
    product_id = input("Enter the ID of the product you want to add to your cart: ")
    quantity = int(input("Enter the quantity: "))
    
    # check if the product is available and the quantity is valid
    cursor.execute("SELECT P_quantity FROM product WHERE ProId=%s", (product_id,))
    product_stock = cursor.fetchone()[0]
    if product_stock < int(quantity):
        print("Sorry, the product is out of stock.")
    # add the product to the cart
    cursor.execute("INSERT INTO cart (CustId, pro_quan, ProId) VALUES (%s, %s, %s)", (customer_id, quantity, product_id))
    BG.commit()
    print("Item added to cart.")

def do_payment():
    customer_id=cid
    print("Choose a payment method:")
    print("1. UPI")
    print("2. Online Banking")
    print("3. debit card")
    print("4. COD")
    method = input("Enter your payment choice: ")
    if method == "1":
        amount = input("Enter the amount: ")
        cart_id = input("Enter the cartid: ")
        cursor.execute("INSERT INTO payment ( Amount, Pay_type,CartId,CustId) VALUES (%s, %s,%s, %s)", ( amount, "upi",cart_id,customer_id))
        BG.commit()
        print("Payment successful!")
    elif method == "2":
        amount = input("Enter the amount: ")
        cart_id = input("Enter the cartid: ")
        cursor.execute("INSERT INTO payment ( Amount, Pay_type,CartId,CustId) VALUES (%s, %s,%s, %s)", ( amount, "netbanking",cart_id,customer_id))
        BG.commit()
        print("Payment successful!")
    elif method == "3":
        amount = input("Enter the amount: ")
        cart_id = input("Enter the cartid: ")
        cursor.execute("INSERT INTO payment ( Amount, Pay_type,CartId,CustId) VALUES (%s,%s, %s, %s)", ( amount, "debit card",cart_id,customer_id))
        BG.commit()
        print("Payment successful!")
    elif method == "4":
        amount = input("Enter the amount: ")
        cart_id = input("Enter the cartid: ")
        cursor.execute("INSERT INTO payment ( Amount, Pay_type,CartId,CustId) VALUES (%s,%s, %s, %s)", ( amount, "cash",cart_id,customer_id))
        BG.commit()
        print("Payment successful!")

while(True):
    print('\nWelcome to bigmart! You are in home section now \n')
    print('choose user type\n')
    print('1.customer \n2.admin \n3.employee \n4.supplier \n5.exit')
    t=int(input('enter user type: '))
    if(t==1): #xxxxxxxxxxxxxxxx customer xxxxxxxxxxxxxxx
        while(True):
            print('Hello customer! \n')
            print('1. Create new customer account \n2.Login as existing customer\n3.Home\n')
            A=int(input())
            if (A==1):
                create_customer()
            elif (A==2):
                r=cust_login()
                
                if(r):
                    while(True):
                        print('\nchoose functionality')
                        print('1.list of products in furniture category \n \
2.product details whose price is less than 1000 \n \
3.product details whose price is less than dark fantasy \n \
4.list of electronic appliances whose discput is between 30% and 40% \n \
5.cheapest product price and costliest product price in cvategories 1 - 50 \n \
6.List details of all Products of furniture Category \n \
7.Add to cart \n \
8.Do payment \n \
9.back')
                        a=int(input('choose functionality: '))
                        if(a==1): 
                            f1()
                        elif(a==2):
                            f2()
                        elif(a==3):
                            f3()
                        elif(a==4):
                            f10()
                        elif(a==5):
                            f13()
                        elif(a==6):
                            List_Prod()
                        elif(a==7):
                            add_to_cart()
                        elif(a==8):
                            do_payment()
                        elif(a==9):
                            break
                elif (r==0):
                    break

            elif(A==3):
                break
    elif (t==2): #xxxxxxxxxxxxxxxxx admin xxxxxxxxxxxx
        while(True):
            print('Hello admin! \n')
            xy=admin_login()
            if(xy):
                print('\nchoose funtionality')
                print('1.all order details list \n \
2.list of employees whose salary is more than 10000 \n \
3.list of available delivery employees \n \
4.names of admin who are manager and architect \n \
5.average salary and total gross salary of all employees \n \
6.list of subscription types whose subscribers count is more than 20 \n \
7.list of customers who placed orders between amount 100000 and 200000 \n \
8.Name of Customers who have placed order between 100000 and 200000 \n \
9.list of total bill of delivered orders an delivery agent collected from particular customers in certain time \n \
10.Home\n')
                b=int(input('choose functionality: '))
                if (b==1): 
                    f4()
                
                elif (b==2):
                    f6()
                
                elif (b==3):
                    f7()
                
                elif(b==4): 
                    f9()
                
                elif(b==5):
                    f11()

                elif(b==6):
                    f15()
                elif(b==7):
                    f16()
                    
                elif(b==8):
                    Order_Prod()
                    
                elif(b==9):
                    List_delivered_orders()
                elif(b==10):
                    break
                
            elif(xy==0):
                break
    elif (t==3): #xxxxxxxxxxxxxxx employee xxxxxxxxxxxxxxxx
        while(True):
            print('Hello employee! \n')
            ac = emp_login()
            if(ac):
                print('\nchoose functionality')
                print('1.list of prime subcribers \n \
2.supplier details of particular order id \n \
3.list of emplyees who doesnot have last name \n \
4.List of all Employees who are available for delivery \n \
5.Get the Status, Delivery Time, Bill & Details of delivery agent for the current Order of a customer \n \
6.Home')
                c=int(input('Enter query number: '))
                if (c==1): 
                    f5()
                elif (c==2): 
                    f8()
                
                elif (c==3): 
                    f14()
                elif (c==4): 
                    List_available_Emps()
                
                elif (c==5):  
                    Curr_Order()
                
                elif(c==6):
                    break
                
            elif(ac==0):
                break
    elif (t==4): #xxxxxxxxxxxxxxx supplier xxxxxxxxxxxxxxxx
        while(True):
            print('Hello supplier! \n')
            bd = supp_login()
            if(bd!=0):
                print('1.count of products added in carts till now of category bevrages \n \
2.list of products quantity purchased by each subscription type \n \
3.Home')
                d=int(input('Enter query number: '))
                if d==1: 
                    f12()
                elif d==2:
                    Prod_quan_by_subs()
                elif d==3:
                    break
            elif(bd==0):
                break
    elif(t==5): #exit
        print('exited application successfully! \n')
        break
    
cursor.close()
DB.close()
BG.close()

