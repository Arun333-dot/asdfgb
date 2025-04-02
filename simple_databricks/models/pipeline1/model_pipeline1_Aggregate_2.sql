{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Aggregate_2_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH Deduplicate_2 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

),

Aggregate_2 AS (

  SELECT * 
  
  FROM Deduplicate_2 AS in0

)

SELECT *

FROM Aggregate_2
