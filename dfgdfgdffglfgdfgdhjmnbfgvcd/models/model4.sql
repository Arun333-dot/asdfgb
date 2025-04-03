WITH seed1 AS (

  SELECT * 
  
  FROM {{ ref('seed1')}}

)

SELECT *

FROM seed1
