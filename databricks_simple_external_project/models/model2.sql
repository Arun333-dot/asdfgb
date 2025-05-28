WITH m1 AS (

  SELECT * 
  
  FROM {{ ref('m1')}}

)

SELECT *

FROM m1
