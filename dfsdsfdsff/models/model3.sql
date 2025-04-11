WITH bigint_data AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'bigint_data') }}

)

SELECT *

FROM bigint_data
