-- Consider the following table

-- Transaction_Table
-- Column Names
-- Customer_Id : Customer_ID of the customer
-- Transaction_Date : Date of Transaction
-- Transaction_Status : Status of Transaction ('Sucess','Failed')
-- Transaction_Amount : Amount for the transaction

-- CUSTOMER_DETAILS
-- Customer_Id : Customer_ID of the customer
-- Customer_Name : Name of the customer
-- Customer_Join : Date when customer joined the platform


Q1. Find all the details joining the two tables Transaction_Table and CUSTOMER_DETAILS

Q2. Find the Name of the customer with the highest Transaction Amount ( Sucessfull one )

====================================================================
Solution
====================================================================

S1. SELECT * FROM Transaction_Table TT
    JOIN CUSTOMER_DETAILS CD ON TT.Customer_ID = CD.Customer_ID


S2. SELECT Customer_Name FROM CUSTOMER_DETAILS CD
    JOIN Transaction_Table TT ON CD.Customer_ID = TT.Customer_ID
    WHERE Transaction_Status LIKE ('Sucess')
    ORDER BY Transaction_Amount DESC
    LIMIT 1

