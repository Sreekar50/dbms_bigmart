## Project — BigMart RDBMS

A SQL-driven back-end for an online retail store supporting four roles—Customer, Admin, Employee, and Supplier—plus a set of automatic triggers that keep data consistent and business rules enforced.

---

### ⭐ Built-in Triggers
| # | Business Rule | SQL Mechanism |
|---|---------------|---------------|
| 1 | **Update stock** immediately after a successful payment | `TRIGGER` |
| 2 | **Increase discounts** automatically during a sales season | `TRIGGER` |
| 3 | **Refund customer** if an order is late | `TRIGGER` |
| 4 | **Alert staff/suppliers** when product quantity falls below 100 | `TRIGGER` |

---

### 🛒 Customer-Facing Queries & Actions
| # | Description | Key SQL Feature |
|---|-------------|-----------------|
| 1 | List products in the **Furniture** category | `JOIN` |
| 2 | Show product details where **price < 1000** | `ORDER BY` |
| 3 | Show product details of item **“Dark Fantasy”** | `SELECT … WHERE name = 'Dark Fantasy'` |
| 4 | List electronic appliances with **30 %–40 % discount** | `BETWEEN` |
| 5 | Fetch the **cheapest & costliest** product prices in categories 1 – 50 | `MIN`, `MAX` |
| 6 | List **all Furniture products** with extended details | `JOIN … ON` |
| 7 | **Add to cart** | `INSERT` |
| 8 | **Make payment / checkout** | `UPDATE`, `INSERT` |

---

### 🔧 Admin-Facing Queries
| # | Description | Key SQL Feature |
|---|-------------|-----------------|
| 1 | Show **all orders** | `SELECT *` |
| 2 | List employees whose **salary > 10000** | `WHERE` |
| 3 | View currently **available delivery employees** | `WHERE status = 'available'` |
| 4 | Names of admins who are **both Manager _and_ Architect** | `UNION` |
| 5 | **Avg. & Total salaries** of all employees | `AVG`, `SUM` |
| 6 | Subscription types with **> 20 subscribers** | `GROUP BY`, `HAVING`, `ORDER BY` |
| 7 | Customers with **orders ₹100 000 – ₹200 000** | `INNER JOIN`, `BETWEEN`, `ORDER BY` |
| 8 | Names of those customers (same range) | `INNER JOIN`, `BETWEEN`, `ORDER BY` |
| 9 | Total bill amounts collected by each delivery agent in a time range | `GROUP BY` |

---

### 👔 Employee-Facing Queries
| # | Description | Key SQL Feature |
|---|-------------|-----------------|
| 1 | List all **Prime subscribers** | `WHERE subscription = 'Prime'` |
| 2 | Supplier details for a **given order ID** | `JOIN` |
| 3 | Employees **without a last name** | `WHERE last_name IS NULL` |
| 4 | Employees currently **available for delivery** | `WHERE status = 'available'` |
| 5 | Status, delivery time, bill & agent details for a customer’s current order | `JOIN`, `WHERE` |

---

### 🏭 Supplier-Facing Queries
| # | Description | Key SQL Feature |
|---|-------------|-----------------|
| 1 | Count of **beverages** items currently in carts | `INNER JOIN`, `COUNT` |
| 2 | Quantity of each product **purchased per subscription type** | `JOIN`, `GROUP BY` |

---

### 📊 Cross-Functional Analytics
| # | Description | Key SQL Feature |
|---|-------------|-----------------|
| 1 | Total salary expenditure by **gender & age** | `ROLLUP` |
| 2 | Transaction amounts paid via **Cash vs Debit Card** | `ROLLUP`, `HAVING` |
| 3 | Total **account balance per subscription type** | `GROUP BY` |

---

### 🗄️ Tech Stack
* **MySQL** / **MariaDB** (tested with MySQL 8.0)
* SQL scripts organized in `/sql` directory
* CLI interface written in **Python 3.11**

> **Tip:** Run `source schema.sql` followed by `source demo_data.sql` to bootstrap the database quickly.

---


