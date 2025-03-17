{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Filter_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH Filter_1 AS (

  SELECT * 
  
  FROM `` AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
