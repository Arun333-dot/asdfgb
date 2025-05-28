WITH model AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'model') }}

)

SELECT *

FROM model
