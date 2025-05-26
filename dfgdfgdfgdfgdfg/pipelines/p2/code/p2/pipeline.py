from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from p2.config.ConfigStore import *
from p2.functions import *
from prophecy.utils import *
from p2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_arun123_boolean_data = arun123_boolean_data(spark)
    df_reformat_id_column = reformat_id_column(spark, df_arun123_boolean_data)
    sdfsdf(spark, df_reformat_id_column)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("p2").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/p2")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/p2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
