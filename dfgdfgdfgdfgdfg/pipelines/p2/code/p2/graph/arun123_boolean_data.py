from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2.config.ConfigStore import *
from p2.functions import *

def arun123_boolean_data(spark: SparkSession) -> DataFrame:
    return spark.read.table("`hive_metastore`.`arun123`.`boolean_data`")
