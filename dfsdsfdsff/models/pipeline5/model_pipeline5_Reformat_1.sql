{{
  config({    
    "materialized": "table",
    "alias": "call_center",
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
    {{ var('Name') }} AS Name,
    {{ var('Age') }} AS Age,
    {{ var('ID') }} AS ID
  
  FROM million_records AS in0

)

SELECT *

FROM Reformat_1
