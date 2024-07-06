import mysql.connector
import datetime

DB = mysql.connector.connect(
  host="localhost",
  user="root", #hostname
  password="Sreekar@33", #password
  database="bigmart1"
)

cursor = DB.cursor()

#xxxxxxxxxxxxxxxxxxxxxxx EMBEDDED FUNCTIONS xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def List_Prod(): #List details of all Products of a certain Category
    #print("details of all Products of a certain Category")
    query = "select product.Pro_name, product.P_price, product.P_quantity, product.P_discount, product.P_expiry \
            from product \
            join category \
            on (product.CatId = category.CatId) and category.Cat_name = 'furniture'"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def List_available_Emps(): #List of all Employees who are available for delivery
    #print("List of all Employees who are available")
    query = "select * \
            from employee \
            where Del_avail = 'Yes'"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        if x is None:
            print("Empty")
        print(x)
    print("\n")
    
def Order_Prod(): #Name of Customers who have placed order between an amount range
    #print("printing Name of Customers who have placed order between 100000 and 200000")
    query = "select distinct c1.cus_firstname, c1.cus_middlename, c1.cus_lastname \
              from customer as c1 \
                inner join order_details as o \
                on c1.CustId = o.CustId \
                and o.Bill between 100000 and 200000 \
                order by c1.cus_firstname"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def Curr_Order(): #Get the Status, Delivery Time, Bill & Details of delivery agent for the current Order of a customer
    #print("printing current orders which are getting packed")
    query = "select O.Status, O.Delivery_Time, O.Bill, O.Delivery_Agent_Name, O.Delivery_Agent_Phone_No\
             from order_details as O\
             where O.Status='packing'"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in list(result):
        for i in range(0,4):
            a = "{["+ str(i)+ "]}"
            print(a.format(x), end=" ")
        print("")
    print("\n")
    

#xxxxxxxxxxxxxxxxxxxxxxxxxxxx OLAP xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def List_delivered_orders(): # list of total bill of delivered orders an delivery agent collected from particular customers in certain period of time
    #print("list of total bill of delivered orders collected from a customer")
    query = "SELECT Delivery_Agent_Id, CustId, SUM(Bill) AS total_bill\
            FROM order_details\
            WHERE Status = 'delivered' AND Order_Date between '2022-05-01' AND '2022-12-31'\
            GROUP BY Delivery_Agent_Id, CustId"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def Prod_quan_by_subs(): #list of products quantity purchased by each subscription type
    #print("list of products quantity purchased by each subscription type")
    query = "SELECT c.Subcription_Type AS Subscription_Type, SUM(cart.P_quantity) AS Product_Quantity \
            FROM customer as c \
            JOIN cart ON c.CustId = cart.CustId\
            GROUP BY c.Subcription_Type"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def Prod_quan_by_category(): #lists total product quantities grouped by category Id having discount in specific ranges
    #print("list of total product quantity grouped by category")
    query = "SELECT CatId,\
            SUM(CASE WHEN P_discount between 20 and 35 THEN P_quantity ELSE 0 END) AS `less discount`,\
            SUM(CASE WHEN P_discount between 35 and 50 THEN P_quantity ELSE 0 END) AS `normal discount`,\
            SUM(CASE WHEN P_discount > 50 THEN P_quantity ELSE 0 END) AS `more discount`\
            FROM product\
            GROUP BY CatId"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def employe_salary(): # total salary of employes according to their gender and age
    #print("Total salary of employees grouped by gender & age")
    query = "SELECT Emp_gender, Emp_age, SUM(Emp_salary) AS total_salary \
            FROM employee\
            GROUP BY Emp_gender, Emp_age WITH ROLLUP"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

def pay_method(): #list of each transaction amount paid through cash or debit card
    #print("list of each transaction amount paid through cash or debit card")
    query = "SELECT  PayId,Pay_type, CustId, SUM(Amount) AS total_amount\
            FROM payment\
            GROUP BY PayId,Pay_type,CustId WITH ROLLUP\
            HAVING (Pay_type IN ('cash', 'debit card') )\
            ORDER BY  PayId DESC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
def acc_balance(): #calculates total account balance of each subcription type
    #print("total account balance of each subcription type")
    query = "SELECT  Subcription_Type, SUM(Account_Balance) AS total_balance\
            FROM customer\
            GROUP BY Subcription_Type\
            HAVING (Subcription_Type IN ('prime', 'elite') )\
            ORDER BY  total_balance DESC;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")
    
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxx Triggers xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# A trigger which alerts the responsible employees/supplier when the quantity of a product available goes below 100
def low_stock_alert():
    query = "DELIMITER //\
            CREATE TRIGGER low_amount_alert_trigger\
            AFTER UPDATE ON product\
            FOR EACH ROW\
            BEGIN\
                IF (NEW.P_quantity < 100) THEN \
                    INSERT INTO system_logs (log_type, log_message)\
                    VALUES ('low_stock', CONCAT('Low stock alert for product ', NEW.Pro_name, \
                            '. Only ', NEW.P_quantity, ' left in stock.'));\
                END IF;\
            END //\
            DELIMITER ;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

# Refund customer if the order does not reach them on time.
def refund_cust():
    query = "DELIMITER //\
            CREATE TRIGGER refund_trigger\
            AFTER UPDATE ON Order_details\
            FOR EACH ROW\
            BEGIN\
                IF curdate()>NEW.Order_Date THEN\
                    UPDATE Customer \
                    SET Account_Balance = Account_Balance + NEW.Bill \
                    WHERE CustId = NEW.CustId;\
                END IF;\
            END //\
            DELIMITER ;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

# Increase discount during sale season
def sale_time():
    query = "DELIMITER //\
            CREATE TRIGGER seasonal_sales_trigger\
            AFTER INSERT ON product\
            FOR EACH ROW\
            BEGIN\
                IF curdate() BETWEEN '2020-12-25' AND '2024-01-01' THEN  \
                    UPDATE product\
                    SET product.P_discount = product.P_discount + 0.1\
                    WHERE product.ProId = NEW.ProId;\
                END IF;\
            END //\
            DELIMITER ;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")

# A trigger which deceases the stock after payment
def stock_update():
    query = "DELIMITER //\
            CREATE TRIGGER quantity_update_after_payment\
            AFTER UPDATE ON product\
            FOR EACH ROW\
            BEGIN\
                UPDATE product\
                SET product.P_quantity = product.P_quantity - NEW.Cart.P_quantity\
                WHERE ProId = NEW.ProId;\
            END //\
            DELIMITER ;"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("\n")


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx




cursor.close()
DB.close()