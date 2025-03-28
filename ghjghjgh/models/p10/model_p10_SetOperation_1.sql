{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p10_post_SetOperation_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH SetOperation_1 AS (

  SELECT * 
  
  FROM `` AS in0
  
  UNION
  
  SELECT * 
  
  FROM `` AS in1

)

SELECT *

FROM SetOperation_1
