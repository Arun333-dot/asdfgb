WITH sqlmodel AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'sqlmodel') }}

)

SELECT *

FROM sqlmodel
