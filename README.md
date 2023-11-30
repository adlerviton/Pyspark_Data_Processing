# Databricks ETL Pipeline for Automotive Data
Databricks ETL (Extract Transform Load) Pipeline
[![CI](https://github.com/adlerviton/Databricks_ETL_Pipeline/actions/workflows/python.yml/badge.svg)](https://github.com/adlerviton/Databricks_ETL_Pipeline/actions/workflows/python.yml)

## Background:
#### Purpose
This project aims to perform ETL operations with a pipeline on Databricks using Spark SQL. This will allow for frequently changing data to be frequently ingested to a database and automatically analyzed in real-time or on a scheduled basis. Each of the following scripts are held in the ETL_Databricks_Notebooks folder and represent separate databricks notebooks. 

#### Advantages of Delta Lake for data storage
Using a Delta Lake, a storage layer that sits atop a data lake, gives the following additional benefits:

- Time Travel: Allows querying data at different points in time, aiding historical analysis and auditing.

- Reliability and Consistency: Ensures data reliability with ACID transactions, which are critical when the data is updated from multiple concurrent sources.

- Schema Evolution: Flexibility to modify schemas without disrupting pipelines, accommodating changing business needs.

- Unified Processing: Seamlessly handles both batch and streaming data, enabling comprehensive analysis across different data types.

- Optimized Performance: Improves storage efficiency and query performance.

## Databricks Pipeline Flow:
**Error handling is pervasive throughout, a major advantage of spark SQL, it can easily identify error with data as it is automatically ingested.**

### 1: Extract
The first step is to extract from an external source, in this case, from the Auto.csv file in this repository. This creates a spark session and creates a spark table from the csv. 
![ETL Operations](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Ingest.png)

### 2: Transform
It then makes some changes and creates a new filtered table. In this table, it only keeps cars with an "origin" value of 1, corresponding to American-made cars. It also dropped the "year" column just because why not.
![ETL Operations](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Transform1.png)

#### Read
It also shows some of the transformed table to make sure it looks correct, so if there is an error with the final analysis but no error messages, it can help for spot-checking data without touching the tables.
![ETL Operations](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Read_Transformation.png)

### 3: Load
It then saves the transformed spark Dataframe as a Delta table called `my_delta_table`.
![ETL Operations](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Load.png)

### 4: Analysis
The last step of the pipeline shows you can automatically do analysis and produce real-time visualizations that will update on a scheduled basis. Below, I just put a simple bar chart for average weight as a function of number of cylinders in the car. You can see that at the moment, this set of cars shows an average weight increase as cylinders increase. If the data in the external source changed with time, the visualization would also change automatically. If your company was producing a car and needed to decide how many cylinders to use in the engine, this would help decide once the car's final weight is estimated.
![ETL Operations](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Auto_Visualization.png)

## Running the Pipeline as a Scheduled Job: 

#### Create Job
First, a job is created that links all the different parts together. It is better to keep each notebook separately rather than running all parts as one script, so if there is an issue, it is much easier to see where it happened. 
![Job Stuff](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Job.png)

#### Schedule Job
Then, the job can be scheduled as frequently as desired and at any desired time. Below, both a manual and scheduled successful job run are demonstrated:
![Job Stuff](https://github.com/adlerviton/Databricks_ETL_Pipeline/blob/main/DB_ETL_Images/Job_Schedule.png)


