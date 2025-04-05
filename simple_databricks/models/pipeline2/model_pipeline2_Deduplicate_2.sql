{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline2_post_Deduplicate_2_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH Deduplicate_2 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_2
