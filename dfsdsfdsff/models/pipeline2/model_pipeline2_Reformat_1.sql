{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline2_post_Reformat_1_0",
    "database": "Tanmay",
    "schema": "default"
  })
}}

WITH million_records AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'million_records') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM million_records AS in0

)

SELECT *

FROM Reformat_1
