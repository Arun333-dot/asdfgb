{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p1_post_Intersect_1_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH Intersect_1 AS (

  SELECT * 
  
  FROM `` AS in0
  
  INTERSECT
  
  SELECT * 
  
  FROM `` AS in1

)

SELECT *

FROM Intersect_1
