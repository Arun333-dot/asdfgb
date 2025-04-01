WITH seed1 AS (

  SELECT * 
  
  FROM {{ ref('seed_prophecy')}}

)

SELECT *

FROM seed1
