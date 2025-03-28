WITH boolean_data AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'boolean_data') }}

)

SELECT *

FROM boolean_data
