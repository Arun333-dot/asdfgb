from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2.config.ConfigStore import *
from p2.functions import *

def select_id(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("ID"))
