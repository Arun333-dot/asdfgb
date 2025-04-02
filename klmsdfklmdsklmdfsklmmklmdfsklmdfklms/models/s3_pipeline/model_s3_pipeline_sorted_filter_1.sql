{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_s3_pipeline_post_sorted_filter_1_0",
    "database": "tanmay",
    "schema": "default"
  })
}}

WITH S3Source_0_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_s3_pipeline_source', 'prophecy__temp_s3_pipeline_pre_Reformat_1_1_0') }}

),

Reformat_1_1 AS (

  SELECT * 
  
  FROM S3Source_0_1 AS in0

),

S3Source_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_s3_pipeline_source', 'prophecy__temp_s3_pipeline_pre_Reformat_1_0') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM S3Source_0 AS in0

),

joined_reformatted_data AS (

  SELECT 
    in0._c0 AS _c0,
    in0._c1 AS _c1,
    in0._c2 AS _c2,
    in0._c3 AS _c3,
    in0._c4 AS _c4,
    in0._c5 AS _c5,
    in0._c6 AS _c6,
    in0._c7 AS _c7,
    in0._c8 AS _c8,
    in0._c9 AS _c9
  
  FROM Reformat_1 AS in0
  INNER JOIN Reformat_1_1 AS in1
     ON in1._c0 = in1._c0

),

Filter_1 AS (

  SELECT * 
  
  FROM joined_reformatted_data AS in0
  
  WHERE true

),

sorted_filter_1 AS (

  SELECT * 
  
  FROM Filter_1 AS in0
  
  ORDER BY _c0 ASC NULLS FIRST, _c1 ASC NULLS FIRST

)

SELECT *

FROM sorted_filter_1
