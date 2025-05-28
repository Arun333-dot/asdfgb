{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Reformat_2_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH prophecy__temp_pipeline1_post_SFTPSource_0_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline1_source', 'prophecy__temp_pipeline1_post_SFTPSource_0_0') }}

),

Reformat_2 AS (

  SELECT * 
  
  FROM prophecy__temp_pipeline1_post_SFTPSource_0_0 AS in0

)

SELECT *

FROM Reformat_2
