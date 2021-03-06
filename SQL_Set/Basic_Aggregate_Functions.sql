-- Consider the following table
-- Transaction_Table
-- Column Names
-- Customer_Id : Customer_ID of the customer
-- Transaction_Date : Date of Transaction
-- Transaction_Status : Status of Transaction ('Sucess','Failed')
-- Transaction_Amount : Amount for the transaction


Q1. For the Transaction_Table, find the highest transaction value (Sucessfull)


Q2. Find the total transaction done for the date('2019-01-01') split by sucessful and falied transaction


====================================================================
Solution
====================================================================

S1. SELECT MAX(Transaction_Amount) FROM Transaction_Table

S2. SELECT Transaction_Status, SUM(Transaction_Amount) FROM Transaction_Table
GROUP BY Transaction_Status
