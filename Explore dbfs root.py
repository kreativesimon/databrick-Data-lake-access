# Databricks notebook source
# MAGIC %md
# MAGIC # Explore dbfs root
# MAGIC 1. List all the folders in DBFS
# MAGIC 2. Interact with DBFS file browser
# MAGIC 3. Upload file into DBFS

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('/FileStore'))

# COMMAND ----------

display(spark.read.csv('dbfs:/FileStore/circuits__1_.csv'))

# COMMAND ----------


