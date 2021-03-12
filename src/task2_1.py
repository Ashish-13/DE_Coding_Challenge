#Part 2 Task 1

#Import Modules
from pyspark.sql import SparkSession

#Create a spark session
spark = SparkSession.builder.appName("AirBnB").getOrCreate()

#Load parquet file into dataframe
airbnb_Data = spark.read.parquet("C:\\Users\\Ashish\\Desktop\\Truata\\airbnbdata.parquet")