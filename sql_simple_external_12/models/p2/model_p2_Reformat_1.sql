{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p2_post_Reformat_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH SFTPSource_2 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p2_source', 'prophecy__temp_p2_pre_Reformat_1_0') }}

),

Reformat_1 AS (

  SELECT 
    `@id` AS `@id`,
    author AS author,
    title AS title,
    genre AS genre,
    price AS price,
    publish_date AS publish_date,
    data_type AS data_type,
    data_value AS data_value,
    description AS description
  
  FROM SFTPSource_2 AS in0

)

SELECT *

FROM Reformat_1
