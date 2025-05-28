{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p4_post_Deduplicate_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH Deduplicate_1 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_1
