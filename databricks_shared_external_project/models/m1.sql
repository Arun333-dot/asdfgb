WITH tables AS (

  SELECT * 
  
  FROM {{ source('main.information_schema', 'tables') }}

)

SELECT *

FROM tables
