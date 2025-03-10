{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p3_post_Limit_1_0",
    "database": "qa_database",
    "schema": "qa_prophecy"
  })
}}

WITH Limit_1 AS (

  SELECT * 
  
  FROM "" AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
