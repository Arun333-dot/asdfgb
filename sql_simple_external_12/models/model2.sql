WITH million_records AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'million_records') }}

),

million_records_1 AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'million_records') }}

)

SELECT *

FROM million_records
