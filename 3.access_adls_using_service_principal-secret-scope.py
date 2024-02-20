# Databricks notebook source
# MAGIC %md
# MAGIC #### Acess azure Data Lake using service principal
# MAGIC ## steps to follow
# MAGIC 1. Register Azure AD Application / service principal
# MAGIC 2. Generate a secret /password for the application
# MAGIC 3. set spark config with App/Client id,Directory/Tenant id and secret
# MAGIC 4. Assign role 'storage blob contributor to the data lake

# COMMAND ----------

client_id = dbutils.secrets.get(scope= 'formula1-scope', key='formula1-app-cleint-id')
tenant_id = dbutils.secrets.get(scope= 'formula1-scope', key='formula1-app-tenant-id')
client_secret = dbutils.secrets.get(scope= 'formula1-scope', key='formula1-app-cleint-secret')

# COMMAND ----------



spark.conf.set("fs.azure.account.auth.type.adlsformular01.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.adlsformular01.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.adlsformular01.dfs.core.windows.net", "client_id")
spark.conf.set("fs.azure.account.oauth2.client.secret.adlsformular01.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.adlsformular01>.dfs.core.windows.net", f"https://login.microsoftonline.com/(tenant_id)/oauth2/token")

# COMMAND ----------


