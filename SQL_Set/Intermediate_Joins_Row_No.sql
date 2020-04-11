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


-- Banned_CUSTOMER
-- Customer_Id : Customer_ID of the customer
-- Banned : Banned Customer (1 = Banned, 0 = Not Banned)

Q1. Find the Customer Name with the highest transaction value (Successful) and is a banned customer

Q2. Generate a table with 2nd Customer Transaction_Amount (Successful)


====================================================================
Solution
====================================================================

S1. 
SELECT Customer_Name FROM Transaction_Table TT
JOIN CUSTOMER_DETAILS CD ON TT.Customer_ID = CD.Customer_ID
JOIN Banned_CUSTOMER BC ON BC.Customer_ID = CD.Customer_ID
WHERE Banned = 1
AND Transaction_Status LIKE ('Sucess')
ORDER BY Transaction_Amount DESC
LIMIT 1

S2.
SELECT * FROM
(SELECT Customer_ID,ROW_NUMBER(PARTITION BY Customer_ID ORDER BY Transaction_Date ASC) AS R_N FROM Transaction_Table TT
JOIN CUSTOMER_DETAILS CD ON TT.Customer_ID = TT.Customer_ID
WHERE Transaction_Status LIKE ('Sucess'))A
WHERE A.R_N = 2
