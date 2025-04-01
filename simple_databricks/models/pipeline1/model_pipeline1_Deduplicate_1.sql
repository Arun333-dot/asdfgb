{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Deduplicate_1_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH OrchestrationSource_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline1_source', 'prophecy__temp_pipeline1_pre_Deduplicate_1_0') }}

),

Deduplicate_1 AS (

  SELECT DISTINCT *
  
  FROM OrchestrationSource_1 AS in0

)

SELECT *

FROM Deduplicate_1
