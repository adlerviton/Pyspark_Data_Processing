# Databricks notebook source
import pandas as pd
import plotly.express as px

table_name = 'filtered_table'
spark_data = spark.read.table(table_name)

df = spark_data.toPandas()
results = df.groupby(["cylinders"])["weight"].mean().reset_index()
fig = px.bar(results, x="cylinders", y="weight")
fig.show()
