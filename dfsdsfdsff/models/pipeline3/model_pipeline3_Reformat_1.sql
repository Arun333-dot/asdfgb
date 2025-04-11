{{
  config({    
    "materialized": "table",
    "alias": "output_table",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH million_records AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'million_records') }}

),

Reformat_1 AS (

  SELECT 
    {{ var('string') }} AS string_input_Default_Name,
    {{ var('date') }} AS date
  
  FROM million_records AS in0

)

SELECT *

FROM Reformat_1
