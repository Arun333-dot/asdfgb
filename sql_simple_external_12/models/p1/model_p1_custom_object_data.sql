{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p1_post_custom_object_data_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH SFTPSource_2 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p1_source', 'prophecy__temp_p1_pre_custom_object_data_0') }}

),

custom_object_data AS (

  SELECT 
    CUSTOM_OBJECT AS CUSTOM_OBJECT,
    ID AS ID,
    AGE AS AGE
  
  FROM SFTPSource_2 AS in0

)

SELECT *

FROM custom_object_data
