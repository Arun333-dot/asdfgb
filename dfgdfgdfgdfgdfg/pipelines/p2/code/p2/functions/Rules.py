from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def br(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(12312)).otherwise(lit(- 1)).alias("asdasdasd")

@execute_rule
def br_2(id: Column=lambda: col("ID")):
    return when((id == lit(12)), lit(12123)).otherwise(lit(- 1)).alias("asdasdas")
