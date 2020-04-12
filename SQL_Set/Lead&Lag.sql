-- Number_Sequence
-- Sequence_No : Serial Number
-- Var_No  : Arbitary Number 

Q1. Order by Sequence_No, find the difference between the previous record Var_No and present Var_No 
Eg. Sequence_No, Var_No, Diff   
    1             7        0
    2             8        1
    3             6       -2 


Q1. Order by Sequence_No, find the difference between the present record Var_No and record 2 series ahead  
Eg. Sequence_No, Var_No, Diff   
    1             7        1
    2             8        1
    3             6        . 
    4             9        . 

====================================================================
Solution
====================================================================

S1.
SELECT T.*, Var_No - (LAG(Var_No,1) OVER (ORDER BY Sequence_No)) as Diff from Number_Sequence T 

S2.
SELECT T.*, Var_No - (LEAD(Var_No,2) OVER (ORDER BY Sequence_No)) as Diff from Number_Sequence T 