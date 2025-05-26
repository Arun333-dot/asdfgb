from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def br(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(12)).otherwise(lit(- 1)).alias("output")

@execute_rule
def br2(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(122)).otherwise(lit(- 1)).alias("efwsdf")

@execute_rule
def br_2(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(12123)).otherwise(lit(- 1)).alias("asdasdas")

@execute_rule
def br5(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(12)).otherwise(lit(- 1)).alias("aadsas")
