# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

from pyspark.sql import functions as F

df = spark.table("bronze_zastavky_demo")
df = df.dropDuplicates(["id"]).withColumn("datum", F.to_date("datum"))
df.write.mode("overwrite").saveAsTable("silver_zastavky_demo")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
