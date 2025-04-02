{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_ghghhj_post_Deduplicate_1_0",
    "database": "hive_metastore",
    "schema": "default"
  })
}}

WITH Deduplicate_1 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_1
