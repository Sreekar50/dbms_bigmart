#sql queries

import mysql.connector
import datetime

DB = mysql.connector.connect(
  host="localhost",
  user="root", #hostname
  password="Sreekar@33", #password
  database="bigmart1"
)

cursor = DB.cursor()

def f1(): #list of products in furniture category
    query = "select product.Pro_name, product.P_price, product.P_quantity, product.P_discount, product.P_expiry \
            from product \
            join category \
            on (product.CatId = category.CatId) and (category.Cat_name = "'furniture'") ;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f2(): #product details whose price is less than 1000
    query = "select product.Pro_name, product.P_price, product.P_quantity, product.P_discount, product.P_expiry \
            from product \
            where (product.P_price < 1000);"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f3(): #product details whose price is less than dark fantasy
    query = "select A.Pro_name, A.P_price, A.P_quantity, A.P_discount, A.P_expiry \
            from product as A, product as B \
            where (A.P_price < B.P_price)and(B.ProId = 50) \
            ORDER BY A.P_price DESC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f4(): #all order details list
    query = "select order_details.Status, order_details.Delivery_Time, order_details.Bill, \
	        order_details.Delivery_Agent_Name, order_details.Delivery_Agent_Phone_No \
            from order_details;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f5(): #list of prime subcribers
    query = "select * \
            from customer \
            where customer.Subcription_Type = 'prime';"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f6(): #list of employees whose salary is more than 10000
    query = "select * \
            from employee \
            where Emp_salary>10000;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f7(): #list of available delivery employees
    query = "select * from employee where Del_avail = 'Yes';"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def f8(): #supplier details of particular order id
    query = "select supplier.sup_firstname, supplier.sup_middlename, supplier.sup_lastname \
            from supplier join order_details \
            where supplier.SuppId = order_details.Delivery_Agent_Id and order_details.OrderId = 50;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f9(): #names of admin who are manager and architect
    query = "select Name from admin as A \
            where Role = "'Manager'" \
            union \
            select Name from admin as B \
            where Role = "'Architect'";"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")  
    
def f10(): #list of electronic appliances whose discput is between 30% and 40%
    query = "select Pro_name, P_price from product \
            where CatId = 30 and P_discount between 30 and 40;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f11(): #average salary and total gross salary of all employees
    query = "select avg(Emp_salary) as Average_Salary, sum(Emp_salary) as Total_Gross_Salary from employee;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f12(): #count of products added in carts till now of category bevrages
    query = "select count(product.ProId) as No_of_Products_of_Same_Category \
            from product \
            inner join cart \
            on cart.ProId = product.ProId and product.CatId = 7;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f13(): #cheapest product price and costliest product price in cvategories 1 - 50
    query = "select MIN(P_price) as Cheapest_Product, Max(P_price) as Costliest_Product \
            from product \
            where product.CatId between 1 and 50;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f14(): #list of emplyees who doesn't have last name
    query = "select * from employee where employee.Emp_lastname is null;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f15(): #list of subscription types whose subscribers count is more than 20
    query = "SELECT COUNT(CustId), Subcription_Type FROM customer \
            GROUP BY Subcription_Type \
            HAVING COUNT(CustId) > 20 \
            ORDER BY COUNT(CustId) DESC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def f16(): #list of customers who placed orders between amount 100000 and 200000
    query = "SELECT distinct concat(c1.cus_firstname,' ',c1.cus_middlename,' ',c1.cus_lastname) as customer_name \
            FROM customer AS c1 \
            INNER JOIN order_details AS o \
            ON c1.CustId=o.CustId \
                AND o.Bill BETWEEN 100000 and 200000 \
            ORDER BY customer_name;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
    
cursor.close()
DB.close()