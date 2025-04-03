{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline3_post_Except_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH Except_1 AS (

  SELECT * 
  
  FROM `` AS in0
  
  EXCEPT
  
  SELECT * 
  
  FROM `` AS in1

)

SELECT *

FROM Except_1
