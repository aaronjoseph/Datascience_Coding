-- Consider the following table

-- CUSTOMER_DETAILS
-- Customer_Id : Customer_ID of the customer
-- Customer_Name : Name of the customer
-- Customer_Join : Date when customer joined the platform

Q1. Hypothetically speaking, lets say the Customer_Join Column has null values, replace Null with "Not Joined" 
in the output of the table

    Follow-up question : Will COALESCE handle ' ' & 'NA' values?

Q2. Assume there are blank values and 'NA' in the Customer_Join, how do you flag these records, in a different Column
Expected Output : 

Customer_Id, Customer_Name, Customer_Join, Blank_Output, NA_Output
-----------,--------------.--------------, Blank/Not   , Outputs if NA

====================================================================
Solution
====================================================================

S1.
SELECT Customer_ID,Customer_Name,COALESCE(Customer_Join,'Not Joined') as Customer_Join_Date 
FROM CUSTOMER_DETAILS

OR 

SELECT Customer_ID,Customer_Name,ISNULL(Customer_Join,'Not Joined') as Customer_Join_Date 
FROM CUSTOMER_DETAILS

S1. Follow-up : No, Case statements need to be used for this 

S2. 
SELECT Customer_ID, Customer_Name,COALESCE(Customer_Join,"NOT Joined"),
CASE WHEN Customer_Join = " " THEN 'BLANK_VALUE' END AS CASE_WHEN_DATE_EMPTY,
CASE WHEN Customer_Join = "NA" THEN 'BLANK_VALUE' END AS CASE_WHEN_DATE_NA 
FROM CUSTOMER_DETAILS
