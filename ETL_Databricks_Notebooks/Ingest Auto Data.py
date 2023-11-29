# Databricks notebook source
from pyspark.sql import SparkSession
import os

# Create a SparkSession
spark = SparkSession.builder.appName("SparkySesh").getOrCreate()

# Path to save the downloaded file within the Databricks environment
local_path = "/dbfs/tmp/Auto.csv"

# Define the table name
table_name = "my_table"

# Download the file from GitHub to the local path
file_url = "https://github.com/adlerviton/Databricks_ETL_Pipeline/raw/main/Auto.csv"
dbutils.fs.cp(file_url, local_path)

# Read the downloaded CSV file into a Spark DataFrame
try:
    spark_df = spark.read.csv(local_path, header=True, inferSchema=True)
except Exception as e:
    raise RuntimeError(f"Failed to read CSV into Spark DataFrame: {str(e)}")

# Save the Spark DataFrame as a table with error handling
delta_table_path = f"/mnt/data/delta_tables/{table_name}"
try:
    spark_df.write.saveAsTable(table_name, format="csv", mode="overwrite")
    print(f"Spark DataFrame successfully saved as '{table_name}' in CSV format at '{delta_table_path}'.")
except Exception as e:
    raise RuntimeError(f"Failed to save Spark DataFrame as a table: {str(e)}")
