{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Aggregate_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH OrchestrationSource_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline1_source', 'prophecy__temp_pipeline1_pre_Aggregate_1_0') }}

),

Aggregate_1 AS (

  SELECT * 
  
  FROM OrchestrationSource_0 AS in0

)

SELECT *

FROM Aggregate_1
