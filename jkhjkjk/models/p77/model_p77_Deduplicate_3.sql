{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p77_post_Deduplicate_3_0",
    "database": "hive_metastore",
    "schema": "default"
  })
}}

WITH Deduplicate_3 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_3
