{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p8_post_Deduplicate_0_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH Deduplicate_0 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_0
