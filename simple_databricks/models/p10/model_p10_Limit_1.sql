{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p10_post_Limit_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH DatabricksSource_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p10_source', 'prophecy__temp_p10_pre_full_data_extraction_0') }}

),

full_data_extraction AS (

  SELECT 
    id AS id,
    tiny_value AS tiny_value,
    small_value AS small_value,
    big_value AS big_value,
    name AS name,
    is_active AS is_active,
    salary AS salary,
    float_value AS float_value,
    double_value AS double_value,
    binary_data AS binary_data,
    created_at AS created_at,
    created_at_ntz AS created_at_ntz,
    birth_date AS birth_date,
    interval_value AS interval_value,
    interval_seconds AS interval_seconds,
    metadata AS metadata,
    int_array AS int_array,
    float_array AS float_array,
    boolean_array AS boolean_array,
    decimal_array AS decimal_array,
    timestamp_array AS timestamp_array,
    date_array AS date_array,
    struct_array AS struct_array,
    array_of_arrays AS array_of_arrays,
    struct_of_array AS struct_of_array,
    struct_of_array_of_structs AS struct_of_array_of_structs
  
  FROM DatabricksSource_0 AS in0

),

Limit_1 AS (

  SELECT * 
  
  FROM full_data_extraction AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
