WITH seed_prophecy AS (

  SELECT * 
  
  FROM {{ ref('seed_prophecy')}}

)

SELECT *

FROM seed_prophecy
