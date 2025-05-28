package io.prophecy.pipelines.ewrwe.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
