# -*- coding: utf-8 -*-

import math
import streamlit as st
import pandas as pd
import joblib

# Set the page title and icon
st.set_page_config(
    page_title="SQL Practice Notes",
    page_icon="✅",
    layout="wide",
)

# Set the background color to black and text color to white
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('SQL Practice Notes')
st.markdown(
    """
    <style>
    h1 {
        color: green;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Author information
st.write("Author: Siddharth Patondikar")

# SQL SELECT & WHERE section
st.markdown(
    """
    <h2 style="color: red;">SELECT & WHERE</h2>
    <p>In SQL, the SELECT and WHERE clauses are fundamental components used for filtering and selecting data from a database</p>
    <pre>
    <code>
    SELECT first_name, last_name
    FROM employees
    WHERE department = 'HR' AND salary > 50000;
    </code>
    </pre>
    <p>In this example, the SELECT clause specifies the columns (first_name and last_name) to be included in the result set. The WHERE clause filters the rows, ensuring that only employees in the 'HR' department with a salary greater than 50,000 are selected.</p>
    <p>These clauses are essential for retrieving specific data from a database, enabling you to tailor your query results to your precise requirements.</p>
    """,
    unsafe_allow_html=True,
)

# SQL AGGREGATE FUNCTIONS section
st.markdown(
    """
    <h2 style="color: red;">AGGREGATE FUNCTIONS</h2>
    <p>Here are examples of how to use COUNT, SUM, MAX, GROUP BY, and HAVING to aggregate data using SQL code:</p>
    <p>Let's say we have a table named orders with the following columns: order_id, customer_id, order_date, and total_amount.</p>
    <pre>
    <code>
    # COUNT: To count the number of orders for each customer:
    SELECT customer_id, COUNT(order_id) AS order_count
    FROM orders
    GROUP BY customer_id;
    
    # SUM: To calculate the total amount spent by each customer:
    SELECT customer_id, SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id;
    
    # MAX: To find the highest order amount for each customer:
    SELECT customer_id, MAX(total_amount) AS max_order_amount
    FROM orders
    GROUP BY customer_id;
    
    # GROUP BY: To group the results by a specific column (e.g., order_date) and then aggregate:
    SELECT order_date, COUNT(order_id) AS order_count, SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY order_date;
    
    # HAVING: To filter the results of a grouped query based on an aggregate condition (e.g., customers who have spent more than $1,000):
    SELECT customer_id, SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > 1000;
    </code>
    </pre>
    <p>These SQL queries demonstrate how to use aggregate functions (COUNT, SUM, MAX) along with GROUP BY and HAVING to analyze and summarize data in a database.</p>
    """,
    unsafe_allow_html=True,
)

# SQL DISTINCT section
st.markdown(
    """
    <h2 style="color: red;">DISTINCT</h2>
    <p>Let's assume we have a table named employees with the following columns: employee_id, first_name, last_name, and department.</p>
    <pre>
    <code>
    # DISTINCT: To retrieve a distinct list of departments:
    SELECT DISTINCT department
    FROM employees;
    </code>
    </pre>
    <p>This query will return a list of unique department names from the employees table.</p>
    <pre>
    <code>
    # COUNT DISTINCT: To count the number of distinct departments:
    SELECT COUNT(DISTINCT department) AS distinct_department_count
    FROM employees;
    </code>
    </pre>
    <p>This query will return the count of unique department names in the employees table.</p>
    <pre>
    <code>
    # DISTINCT with Multiple Columns: To get distinct combinations of first_name and last_name:
    SELECT DISTINCT first_name, last_name
    FROM employees;
    </code>
    </pre>
    <p>This query will return a list of unique combinations of first names and last names from the employees table.</p>
    <pre>
    <code>
    # COUNT DISTINCT with Multiple Columns: To count the number of distinct employee combinations (first name and last name):
    SELECT COUNT(DISTINCT first_name, last_name) AS distinct_employee_count
    FROM employees;
    </code>
    </pre>
    <p>This query will return the count of unique combinations of first names and last names in the employees table.</p>
    <p>These SQL queries illustrate how to use DISTINCT to retrieve unique values or combinations and COUNT DISTINCT to count the number of unique values or combinations in a table. These operations are valuable for data analysis and reporting when you want to work with distinct elements within your dataset.</p>
    """,
    unsafe_allow_html=True,
)

# SQL JOINS section
st.markdown(
    """
    <h2 style="color: red;">JOINS</h2>
    <p>In SQL, you can use INNER JOIN and OUTER JOIN, including LEFT JOIN, RIGHT JOIN, and FULL JOIN, to combine data from multiple tables based on a related column. Here are explanations of when and where to use them, along with code examples:</p>
    <p>INNER JOIN:</p>
    <ul>
    <li>Use INNER JOIN when you want to retrieve only the rows that have matching values in both tables.</li>
    <li>It returns the intersection of the two tables, filtering out non-matching rows.</li>
    </ul>
    <pre>
    <code>
    # Example:
    SELECT orders.order_id, customers.customer_name
    FROM orders
    INNER JOIN customers ON orders.customer_id = customers.customer_id;
    </code>
    </pre>
    <p>In this query, only orders with matching customer IDs from both the orders and customers tables are returned.</p>
    <p>LEFT JOIN (OUTER JOIN):</p>
    <ul>
    <li>Use LEFT JOIN when you want to retrieve all rows from the left table and the matching rows from the right table. If there's no match in the right table, it returns null values.</li>
    <li>It ensures that all rows from the left table are included in the result.</li>
    </ul>
    <pre>
    <code>
    # Example:
    SELECT customers.customer_name, orders.order_id
    FROM customers
    LEFT JOIN orders ON customers.customer_id = orders.customer_id;
    <p>In this query, all customers are listed, and their orders are included if they have any. If a customer has no orders, null values will be shown for the order_id.</p>
    """,
    unsafe_allow_html=True,
)

