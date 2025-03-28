{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_this_is_simple_project_pipeline_post_Deduplicate_1_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH Deduplicate_1 AS (

  SELECT DISTINCT *
  
  FROM `` AS in0

)

SELECT *

FROM Deduplicate_1
