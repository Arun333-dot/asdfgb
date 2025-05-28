from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def reformatted_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(udf_1(lit(120)).alias("ghfghfg"), udf_2(lit(123123)).alias("sdfsdf"))
