from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ghj.config.ConfigStore import *
from ghj.functions import *
from prophecy.utils import *
from ghj.graph import *

def pipeline(spark: SparkSession) -> None:
    df_arun123_boolean_data = arun123_boolean_data(spark)
    df_reformat_id_column = reformat_id_column(spark, df_arun123_boolean_data)
    sdfsdf(spark, df_reformat_id_column)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("ghj").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ghj")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ghj", config = Config)(pipeline)

if __name__ == "__main__":
    main()
