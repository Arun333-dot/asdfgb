WITH seed_prophecy AS (

  SELECT * 
  
  FROM {{ ref('seed_github')}}

)

SELECT *

FROM seed_prophecy
