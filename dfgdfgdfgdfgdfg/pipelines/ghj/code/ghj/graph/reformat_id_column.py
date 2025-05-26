from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ghj.config.ConfigStore import *
from ghj.functions import *

def reformat_id_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(udf_1(col("ID")).alias("dsfsdfsdfsdf"), udf_4(lit(1000)).alias("sdfsdfsdf"))
