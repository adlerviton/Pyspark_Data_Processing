# Mini project 10 - Pyspark Data Processing with Databricks
[![CI](https://github.com/adlerviton/Databricks_ETL_Pipeline/actions/workflows/python.yml/badge.svg)](https://github.com/adlerviton/Databricks_ETL_Pipeline/actions/workflows/python.yml)

## Background:
#### Purpose
This project aims to perform data processing with pyspark on Databricks using Spark SQL. Each of the following scripts are held in the ETL_Databricks_Notebooks folder and represent separate databricks notebooks. 

## Databricks Pipeline Flow:

### 1: Extract
The first step is to extract from an external source, in this case, from the Auto.csv file in this repository. This creates a spark session and creates a spark table from the csv. 
![ETL Operations](https://github.com/adlerviton/Pyspark_Data_Processing/blob/main/DB_ETL_Images/Ingest.png)

### 2: Transform
It then makes some changes and creates a new filtered table. In this table, it only keeps cars with an "origin" value of 1, corresponding to American-made cars. It also dropped the "year" column just because why not.
![ETL Operations](https://github.com/adlerviton/Pyspark_Data_Processing/blob/main/DB_ETL_Images/Transform1.png)

#### Read
It also shows some of the transformed table to make sure it looks correct, so if there is an error with the final analysis but no error messages, it can help for spot-checking data without touching the tables.
![ETL Operations](https://github.com/adlerviton/Pyspark_Data_Processing/blob/main/DB_ETL_Images/Read_Transformation.png)

### 3: Load
It then saves the transformed spark Dataframe as a Delta table called `my_delta_table`.
![ETL Operations](https://github.com/adlerviton/Pyspark_Data_Processing/blob/main/DB_ETL_Images/Load.png)

### 4: Analysis
The last step of the pipeline shows you can automatically do analysis and produce real-time visualizations that will update on a scheduled basis. Below, I just put a simple bar chart for average weight as a function of number of cylinders in the car. You can see that at the moment, this set of cars shows an average weight increase as cylinders increase. If the data in the external source changed with time, the visualization would also change automatically. If your company was producing a car and needed to decide how many cylinders to use in the engine, this would help decide once the car's final weight is estimated.
![ETL Operations](https://github.com/adlerviton/Pyspark_Data_Processing/blob/main/DB_ETL_Images/Auto_Visualization.png)



