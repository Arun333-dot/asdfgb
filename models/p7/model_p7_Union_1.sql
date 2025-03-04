{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p7_post_Union_1_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH Union_1 AS (

  SELECT * 
  
  FROM `` AS in0
  
  UNION
  
  SELECT * 
  
  FROM `` AS in1

)

SELECT *

FROM Union_1
