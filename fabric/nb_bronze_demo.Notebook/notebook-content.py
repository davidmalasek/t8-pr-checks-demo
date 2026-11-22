# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Bronze: ukázková tabulka
# Ukázkový notebook pro kontroly T8. Zapisuje dvě tabulky s prefixem vrstvy.

# CELL ********************

from pyspark.sql import functions as F

rows = [(1, "Můstek", "2026-11-20"), (2, "Anděl", "2026-11-21")]
df = spark.createDataFrame(rows, ["id", "zastavka", "datum"])
df = df.withColumn("_loaded_at", F.current_timestamp())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.mode("overwrite").saveAsTable("bronze_zastavky_demo")

for table in ["linky", "spoje"]:
    target = f"bronze_{table}_demo"
    df.write.mode("overwrite").saveAsTable(target)

display(spark.table("bronze_zastavky_demo"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
