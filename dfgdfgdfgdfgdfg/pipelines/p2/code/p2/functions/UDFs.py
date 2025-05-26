from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("udf_2", udf_2)
    spark.udf.register("udf_3", udf_3)
    

    try:
        from prophecy.utils import ScalaUtil
        ScalaUtil.initializeUDFs(spark)
    except :
        pass

def udf_2Generator():
    initial = 1000000

    @udf(returnType = IntegerType())
    def func(value=10):
        return (value * value + value - value * 10000 - 10000 / 2)

    return func

udf_2 = udf_2Generator()

def udf_3Generator():
    initial = 100000

    @udf(returnType = IntegerType())
    def func(value=10):
        return (value * value + value - value * 10000 - 10000 / 2 - 200)

    return func

udf_3 = udf_3Generator()
