# Databricks notebook source
# MAGIC %md
# MAGIC #### Acess azure Data Lake using access keys
# MAGIC 1. set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuit.scv

# COMMAND ----------

spark.conf.set(

"fs.azure.account.key.adlsformular01.dfs.core.window.net","a54KESq8DBZkejqrf3sYrepbdbC48+aArlASrTU0XAQXAXZ1mEyig1uTkrZAl19ewjLmtFO1pGXU+AStjZOUcA==")

# COMMAND ----------

spark.conf.set("fs.azure.account.key.adlsformular01.dfs.core.windows.net", "adlsformular01")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@adlsformular01.dfs.core.windows.net"))

# COMMAND ----------


