-- Premise
-- Running total can be useful when we are interested in the total sum
-- at a given points for potential analysis population segementation 
-- and outlier identification

-- Consider the following table

-- City_Power_Useage
-- City : City Name
-- Power-Usage : Numeric Value


Q1. Find the cumulative sum of power_usage all across the table 

====================================================================
Solution
====================================================================

S1.

Select T.*, SUM(Power_Usage) OVER (ORDER BY Power_Usage ROWS UNBOUNDED PRECEEDING) AS CUM_SUM 
FROM City_Power_Useage T 

