WITH test5672 AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.asadas', 'test5672') }}

)

SELECT *

FROM test5672
