from p_5 import *
from p_4 import *

f = True

while(f):
    print('choose user type\n')
    print('1.customer \n2.admin \n3.employee \n4.supplier \n5.exit')
    t=int(input('enter user type: '))
    if(t==1): #xxxxxxxxxxxxxxxx customer xxxxxxxxxxxxxxx
        g= True
        while(g):
            print('Hello customer! \n')
            print('1.list of products in furniture category \n \
                   2.product details whose price is less than 1000 \n \
                   3.product details whose price is less than dark fantasy \n \
                   4.list of electronic appliances whose discput is between 30% and 40% \n \
                    5.cheapest product price and costliest product price in cvategories 1 - 50 \n \
                    6.List details of all Products of a certain Category \n \
                    7.')
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
            
                
        
    elif (t==2): #xxxxxxxxxxxxxxxxx admin xxxxxxxxxxxx
        h=True
        while(h):
            print('Hello admin! \n')
            print('1.all order details list \n \
                2.list of employees whose salary is more than 10000 \n \
                3.list of available delivery employees \n \
                4.names of admin who are manager and architect \n \
                5.average salary and total gross salary of all employees \n \
                6.list of subscription types whose subscribers count is more than 20 \n \
                7.list of customers who placed orders between amount 100000 and 200000 \n \
                8.Name of Customers who have placed order between 100000 and 200000 \n \
                9.list of total bill of delivered orders an delivery agent collected from particular customers in certain time')
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
    elif (t==3): #xxxxxxxxxxxxxxx employee xxxxxxxxxxxxxxxx
        k=True
        while(k):
            print('1.list of prime subcribers \n \
                 2.supplier details of particular order id \n \
                 3.list of emplyees who doesnot have last name \n \
                4.List of all Employees who are available for delivery \n \
                5.Get the Status, Delivery Time, Bill & Details of delivery agent for the current Order of a customer')
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
            
            
                
    
    elif (t==4): #xxxxxxxxxxxxxxx supplier xxxxxxxxxxxxxxxx
        m=True
        while(m):
            print('Hello supplier! \n')
            print('1.count of products added in carts till now of category bevrages \n \
                2.list of products quantity purchased by each subscription type \n \
                3.')
            d=int(input('Enter query number: '))
            if d==1: 
                f12()
            
    
    
    elif(t==5): #exit
        f=False
    