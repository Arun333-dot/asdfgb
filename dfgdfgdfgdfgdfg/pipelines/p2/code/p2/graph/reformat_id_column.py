from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2.config.ConfigStore import *
from p2.functions import *

def reformat_id_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(udf_1(col("ID")).alias("dsfsdfsdfsdf"))
