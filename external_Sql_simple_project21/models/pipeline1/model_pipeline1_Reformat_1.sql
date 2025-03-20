{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_pipeline1_post_Reformat_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH prophecy__temp_pipeline1_post_SFTPSource_0_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_pipeline1_source', 'prophecy__temp_pipeline1_post_SFTPSource_0_0') }}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    name AS name,
    email AS email,
    age AS age,
    city AS city,
    country AS country
  
  FROM prophecy__temp_pipeline1_post_SFTPSource_0_0 AS in0

)

SELECT *

FROM Reformat_1
