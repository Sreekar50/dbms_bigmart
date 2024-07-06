In this project, I had created an database that can be used for online retail store. This database serves for different type of users like customer, admin, employee and supplier using different types of sql commands.
inbuilt functionalities:  (specific command_type)
    1.stock update after payment - (trigger)
    2.increase discount during sales season - (trigger)
    3.Refund customer if the order does not reach them on time - (trigger)
    4.alerts the responsible employees/supplier when the quantity of a product available goes below 100 - (trigger)
functionalities served for customer:     (specific command_type)
    1.list of products in furniture category -  (JOIN )
    2.product details whose price is less than 1000 - (ORDER BY)
    3.product details whose price is less than dark fantasy 
    4.list of electronic appliances whose discount is between 30% and 40% 
    5.cheapest product price and costliest product price in categories 1 - 50 
    6.List details of all Products of furniture Category - (JOIN on condition)
    7.Add to cart 
    8.Do payment
functionalities served for admin:   (specific command_type)
    1.all order details list 
    2.list of employees whose salary is more than 10000 
    3.list of available delivery employees 
    4.names of admin who are manager and architect - (UNION)
    5.average salary and total gross salary of all employees - (SUM)
    6.list of subscription types whose subscribers count is more than 20 - (group by, order by)
    7.list of customers who placed orders between amount 100000 and 200000 - (INNER JOIN, ORDER BY)
    8.Name of Customers who have placed order between 100000 and 200000 - (INNER JOIN on condition ORDER BY)
    9.list of total bill of delivered orders an delivery agent collected from particular customers in certain time - (GROUP BY)
functionalities served for employee:      (specific command_type)
    1.list of prime subcribers 
    2.supplier details of particular order id 
    3.list of emplyees who doesnot have last name 
    4.List of all Employees who are available for delivery 
    5.Get the Status, Delivery Time, Bill & Details of delivery agent for the current Order of a customer
functionalities served for supplier:     (specific command_type)
    1.count of products added in carts till now of category bevrages - (INNER JOIN)
    2.list of products quantity purchased by each subscription type - (JOIN, GROUP BY)
some other functionalites:
    total salary of employes according to their gender and age - (ROLL UP)
    list of each transaction amount paid through cash or debit card - (ROLL UP HAVING)
    total account balance of each subcription type - 
