from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType,
)
import pyspark.sql.functions as func

spark = SparkSession.builder.appName("Test").getOrCreate()

myschema = StructType(
    [
        StructField("PassengerId", IntegerType(), True),
        StructField("Survived", IntegerType(), True),
        StructField("Pclass", IntegerType(), True),
        StructField("Name", StringType(), True),
        StructField("Sex", StringType(), True),
        StructField("Age", DoubleType(), True),
        StructField("SibSp", IntegerType(), True),
        StructField("Parch", IntegerType(), True),
        StructField("Ticket", StringType(), True),
        StructField("Fare", DoubleType(), True),
        StructField("Cabin", StringType(), True),
        StructField("Embarked", StringType(), True),
    ]
)

titanic_df = (
    spark.read.format("csv")
    .schema(myschema)
    .option("header", "true")
    .option("path", "/Users/aaronmathew/Desktop/Project/Datascience_Coding/Spark/data/titanic.csv")
    .load()
)

output = (
    titanic_df.select(
        titanic_df.PassengerId, titanic_df.Name, titanic_df.Age, titanic_df.Sex
    )
    .where(titanic_df.Age < 30)
    .withColumn("insert_ts", func.current_timestamp())
    .orderBy(titanic_df.PassengerId)
)

output.count()
output.createOrReplaceTempView("titanic_young_passengers")

spark.sql("select * from titanic_young_passengers").show()