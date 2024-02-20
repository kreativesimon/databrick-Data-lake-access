# Databricks notebook source
# MAGIC %md
# MAGIC #### Acess azure Data Lake using sas token
# MAGIC 1. set the spark config for SAS Token
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuit.scv

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.adlsformular01.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.adlsformular01.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.adlsformular01.dfs.core.windows.net","sp=rl&st=2024-02-19T07:24:16Z&se=2024-02-19T15:24:16Z&spr=https&sv=2022-11-02&sr=c&sig=7WMc8O%2FQIHJxMQvXDwuKSeHU5uv%2FqeeAB28XJCDFMyE%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@adlsformular01.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@adlsformular01.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


