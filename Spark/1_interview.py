"""
Logic to break apart the multiple outputs in
"""


from pyspark.sql.functions import col, explode
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("InterviewApp").getOrCreate()

simpleData = [ (1,["Sagar", "Prajapati"]),
               (2,["Shivam", "Gupta"]),
               (3,["Kunal", "Verma"]),
               (4,["Kim"])]

colums = ["ID","Name"]
df_1 = spark.createDataFrame(data=simpleData, schema=colums)
df_1.show()
df_output = df_1.select(col("ID"), explode(col("Name")).alias("Name"))
df_output.show()