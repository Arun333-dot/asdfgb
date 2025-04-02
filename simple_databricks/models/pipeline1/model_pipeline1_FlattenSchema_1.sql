{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_FlattenSchema_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH FlattenSchema_1 AS (

  SELECT * 
  
  FROM `` AS in0

)

SELECT *

FROM FlattenSchema_1
