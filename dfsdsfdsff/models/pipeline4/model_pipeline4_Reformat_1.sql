{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline4_post_Reformat_1_0",
    "database": "Tanmay",
    "schema": "default"
  })
}}

WITH all_type_databricks_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline4_source', 'prophecy__temp_pipeline4_pre_Reformat_1_0') }}

),

Reformat_1 AS (

  SELECT {{ var('string') }} AS Name
  
  FROM all_type_databricks_1 AS in0

)

SELECT *

FROM Reformat_1
