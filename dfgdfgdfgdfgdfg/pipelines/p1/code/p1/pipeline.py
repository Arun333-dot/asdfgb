from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p1.config.ConfigStore import *
from p1.functions import *
from prophecy.utils import *
from p1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_arun123_boolean_data = arun123_boolean_data(spark)
    df_Reformat_1 = Reformat_1(spark, df_arun123_boolean_data)
    sdfsdf(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("p1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
