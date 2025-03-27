{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline123123213_post_FlattenSchema_1_0",
    "database": "hive_metastore",
    "schema": "default"
  })
}}

WITH WindowFunction_1 AS (

  SELECT * 
  
  FROM `` AS in0

),

FlattenSchema_1 AS (

  SELECT * 
  
  FROM WindowFunction_1 AS in0

)

SELECT *

FROM FlattenSchema_1
