from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ghj.config.ConfigStore import *
from ghj.functions import *

def arun123_boolean_data(spark: SparkSession) -> DataFrame:
    return spark.read.table("`hive_metastore`.`arun123`.`boolean_data`")
