# Databricks notebook source
# MAGIC %md
# MAGIC #### Acess azure Data Lake using sas token
# MAGIC 1. set the spark config for SAS Token
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuit.scv

# COMMAND ----------

formula1dl_demo_sas_token = dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1dl-demo-sas-token')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.adlsformula002.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.adlsformula002.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.adlsformula002.dfs.core.windows.net", formula1dl_demo_sas_token)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@adlsformula002.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@adlsformula002.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


