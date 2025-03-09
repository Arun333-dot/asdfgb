WITH model_1 AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'model') }}

)

SELECT *

FROM model_1
