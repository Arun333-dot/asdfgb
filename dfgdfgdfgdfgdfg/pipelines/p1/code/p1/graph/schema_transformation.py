from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def schema_transformation(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return add_rule(in0, br5())
