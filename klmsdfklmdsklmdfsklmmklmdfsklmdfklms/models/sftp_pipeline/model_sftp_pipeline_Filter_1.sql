{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_sftp_pipeline_post_Filter_1_0",
    "database": "tanmay",
    "schema": "default"
  })
}}

WITH SFTPSource_0_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_sftp_pipeline_source', 'prophecy__temp_sftp_pipeline_pre_Reformat_2_0') }}

),

Reformat_2 AS (

  SELECT * 
  
  FROM SFTPSource_0_1 AS in0

),

SFTPSource_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_sftp_pipeline_source', 'prophecy__temp_sftp_pipeline_pre_Reformat_1_0') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM SFTPSource_0 AS in0

),

Join_1 AS (

  SELECT 
    in0.id AS id,
    in0.name AS name,
    in0.email AS email,
    in0.age AS age,
    in0.city AS city,
    in0.country AS country
  
  FROM Reformat_1 AS in0
  INNER JOIN Reformat_2 AS in1
     ON in1.id = in0.id

),

Limit_1 AS (

  SELECT * 
  
  FROM Join_1 AS in0
  
  LIMIT 10

),

Filter_1 AS (

  SELECT * 
  
  FROM Limit_1 AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
