{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline5_post_Reformat_2_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH OrchestrationSource_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline5_source', 'prophecy__temp_pipeline5_pre_Reformat_2_0') }}

),

Reformat_2 AS (

  SELECT * 
  
  FROM OrchestrationSource_0 AS in0

)

SELECT *

FROM Reformat_2
